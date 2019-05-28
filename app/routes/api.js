
var User = require('../models/user');
var Story = require('../models/story');
var Friend = require('../models/friend');

var config =  require('../../config');

var secretKey = config.secretKey;

var request = require('request');
var url = 'https://api.openweathermap.org/data/2.5/weather?lat=39.792123&lon=30.506522&units=metric&appid=5c79122d65188a78c69598ad07c7c6ea'
 
var jsonwebtoken = require('jsonwebtoken');


function createToken(user){

	var token = jsonwebtoken.sign({

		id: user._id,
		name : user.name,
		username : user.username

	},
	secretKey,
	 {
		expiresIn : 1440
	});


	return token;

}

module.exports = function(app, express , io) {

	var api = express.Router();

	api.get('/all_stories' , function(req,res) {
		Story.find({} , function(err , stories) {
			if(err){
				res.send(err);
				return;
			}
			res.json(stories); 
		});
	});

	api.get('/weather', function(req,res){
		request(url , function(error , response , body){


			weather_json =  JSON.parse(body);

			weather = {
				temperature : Math.round(weather_json.main.temp),
				description : weather_json.weather[0].description,  
			}
		//	weather_data = {weather:weather};
			res.send(weather);
		})
	});

	api.post('/signup' ,  function(req,res){

		var user = new User({

			name : req.body.name,
			username : req.body.username,
			password : req.body.password	

		});

		var token = createToken(user);

		user.save(function(err){
			if(err){
				res.send(err);
				return;
			}
			else{
				res.json({

					success : true,
					message : "User has been created !",
					token : token

			});
			}
		});

	});

	api.get('/users' , function(req ,res){

		User.find({} , function(err , users){
				if(err){
				res.send(err);
				return;
			}
			
				res.json(users);
			
		});
	});

	api.post('/login' , function(req,res){

		User.findOne({

			username: req.body.username


		}).select('name username password').exec(function(err,user){

			if(err) throw err; 

			if(!user){
				res.send({message : "User doesn't exist"});
			}
			else if(user){
				var validPassword = user.comparePassword(req.body.password);

				if(!validPassword){
				res.send({message : "invalid password"});
				
			}
			else{
				

				var token = createToken(user);

				res.json({
					success: true,
					message : "Successfuly Login!",
					token: token
				});
			}
		}
			

				
		});


	});


	api.use(function(req,res,next){

		console.log('Somebody just came to our app!');

		var token = req.body.token || req.param('token') || req.headers['x-access-token'];

		//check token exist

		if(token){
			jsonwebtoken.verify(token,secretKey,function(err,decoded){

				if(err){
					res.status(403).send({success:false , message : "Failed to authecticate token user"});
				}
				else{
					
					req.decoded = decoded;
 
					next();
				}
			});
		}
		 else{
		 	res.status(403).send({success : false , message :"No Token Provided"});
		}
	});

	// Destination

	api.route('/')

		.post(function(req,res){

			var datetime =  new Date();

			var story = new Story({

				creator :  req.decoded.id,
				content :  req.body.content,
				created : datetime,
			});
	
			story.save(function(err , newStory){
				if(err){
					res.send(err);
					return;
				}
				io.emit('story' , newStory)
				res.json({message: "New Story has been created"})

			});

			/*Story.create(req.body , function(err,stori){
				if(err){
					res.send(err);	
				}
				res.json(stori);
			});*/
			
		})

			.get(function(req ,res){

				Story.find({creator:req.decoded.id} , function(err, stories){

					if(err){
						res.send(err);
						return;
					}
					res.json(stories);
				});
			});



		api.post('/recordfriend' , function(req,res){

			var friend = new Friend({
				creator: req.decoded.id,
				description: req.body.description,
				number : req.body.number,
				email : req.body.email,	
			});
			friend.save(function(err,newFriend){
				if(err){
					res.send(err);
					return;
				}

				res.json({
					success : true,
				});
			});
		});

		api.get('/af' , function(req , res) {
			Friend.find({creator:req.decoded.id} , function(err , friends){

		
			   if(err){
					res.send(err);
					return;
				}		
			      res.json(friends);	
			});
		});

		api.post('/getfri' , function(req , res){
			Friend.findOne({
				description : req.body.description
			}).select('number email').exec(function(err,friend){
				if(err) throw err;
				else{
					res.send(friend);
				}
			})
		})

		api.get('/me' , function(req,res){

			res.json(req.decoded);
			
		});



	return api 
}