var pictureNames= ["treeblur.jpg", "fall.jpg", "winter.jpg", "spring.jpg"];
var fontColors = ["white", "white", "black", "#303030"];
var index = 0;

function goBack(){
  index--;
  if(index == -1){
    index = 3;
  }
  document.body.style.backgroundImage = "url('images/" +pictureNames[index] + "')";
  document.body.style.color = fontColors[index];
}

function goForward(){
  index++;
  if(index == 4){
    index=0;
  }
  document.body.style.backgroundImage = "url('images/" +pictureNames[index] + "')";
  document.body.style.color = fontColors[index];

}
