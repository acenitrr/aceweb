
var request1 = new XMLHttpRequest();

request1.onreadystatechange = function(response) {
  if (request1.readyState === 4) {
    if (request1.status === 200) {

      var NoticeJsonList = JSON.parse(request1.responseText);

  //              document.getElementById("notice_marquee").innerHTML='<ul>';
      for(var x=0;x<NoticeJsonList['list'].length;x++)
      {

          document.getElementById("notice_marquee").innerHTML+= '<div class=row><div class="col-sm-12" >'+'<a style="color:#252627" href="'+NoticeJsonList['list'][x].url+'">'+NoticeJsonList['list'][x].title+'</a></div></div></br>';
      }
//                document.getElementById("notice_marquee").innerHTML+='</ul>';

    }
  }}

request1.open('GET', '/notice_get', true);
request1.send();
