

function lname(fn){
      var fn=fn || '';
      var lname=fn.split(',')
      return lname[0]
    }
function fname(fn){
      var fn=fn ||'';
      var fname=fn.split(' ');
      return fname[1]
    }

function extname(fn){
      var fn=fn ||'';
      var fname=fn.split(' ');
      var ext=fname.slice(-1)[0]
      if ((ext=='JR')||(ext=='JR.')||(ext=='SR')||(ext=='SR.')||(ext=='JRA')||(ext=='JRA.')||(ext=='I')||(ext=='II')||(ext=='III')){
        return ext
      }else{
        return ""
      }}
    
function mname(fn){
      var fn=fn ||'';
      var fname=fn.split(' ');
      if (fname.length==3){
        var m=fname[2]
        return m
      }else{
        var m=fname[2]
        return m
      }
        
    }

document.getElementById("btnlogin").click(function(){
  alert('')
})