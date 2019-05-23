var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var FriendSchema = new Schema({

	creator : {type : Schema.Types.ObjectId ,  ref : 'User'},
	description: String,
	number : {type:String , required : true , index: {unique:true}},
	email : String,

});

module.exports = mongoose.model('Friend' , FriendSchema);