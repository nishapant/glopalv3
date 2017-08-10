var pictureNames= ["treeblur.jpg", "fall.jpg", "winter.jpg", "spring.jpg"];
var fontColors = ["white", "white", "black", "#303030"];
var index = 0;

function goBack(){
  index--;
  if(index == -1){
    index = 3;
  }
<<<<<<< HEAD
  document.body.style.backgroundImage = "url('/static/core/images/" +pictureNames[index] + "')";
=======
  document.body.style.backgroundImage = "url('templates/core/" +pictureNames[index] + "')";
>>>>>>> 9e3666e40ad1e4402c2ff0ece2009b436cfe61a1
  document.body.style.color = fontColors[index];
}

function goForward(){
  index++;
  if(index == 4){
    index=0;
  }
<<<<<<< HEAD
  document.body.style.backgroundImage = "url('/static/core/images/" +pictureNames[index] + "')";
=======
  document.body.style.backgroundImage = "url('/templates/core/" +pictureNames[index] + "')";
>>>>>>> 9e3666e40ad1e4402c2ff0ece2009b436cfe61a1
  document.body.style.color = fontColors[index];

}
