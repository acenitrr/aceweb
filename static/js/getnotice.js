
var request = new XMLHttpRequest();

request.onreadystatechange = function(response) {
  if (request.readyState === 4) {
    if (request.status === 200) {

      var NoticeJsonList = JSON.parse(request.responseText);

  //              document.getElementById("notice_marquee").innerHTML='<ul>';
      for(var x=0;x<NoticeJsonList['list'].length;x++)
      {

          document.getElementById("notice_marquee").innerHTML+= '<div class=row><div class="col-sm-12" >'+'<a style="color:#252627" href="'+NoticeJsonList['list'][x].url+'">'+NoticeJsonList['list'][x].title+'</a></div></div></br>';
      }
//                document.getElementById("notice_marquee").innerHTML+='</ul>';

    }
  }}

request.open('GET', '/notice_get', true);
request.send();
