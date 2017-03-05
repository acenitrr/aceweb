
var request2 = new XMLHttpRequest();
request2.onreadystatechange = function(response) {
  if (request2.readyState === 4) {
    if (request2.status === 200) {

      var NoticeJsonList = JSON.parse(request2.responseText);

  //              document.getElementById("notice_marquee").innerHTML='<ul>';
      var first=NoticeJsonList['list'][0];
      var tmpa='<li><time class="cbp_tmtime" datetime='+first.created+'>'
          tmpa+='<span style="color:black;"><b></b></span>'
          tmpa+='<span STYLE="FONT-SIZE:20PX;color:#1c2d3f">'+first.title+'</span></time>'
          tmpa+='<div class="cbp_tmicon cbp_tmicon-screen"></div>'
          tmpa+='<div class="cbp_tmlabel" style="background:#1c2d3f;">'

          tmpa+='<h2>'+first.subtitle+'</h2>'
          tmpa+='<p >'+first.content+'</p></div>'
          </li>
          document.getElementById("announcement_data").innerHTML=tmpa;
      for(var x=1;x<NoticeJsonList['list'].length;x++)
      {
        var xyz=NoticeJsonList['list'][x];
        //alert(xyz.subtitle)
        if(NoticeJsonList['list'][x-1].title!=NoticeJsonList['list'][x].title)
          {
            tmpa='</li>';
          tmpa='<li><time class="cbp_tmtime" datetime='+xyz.created+'>'
          tmpa+='<span style="color:black;"><b></b></span>'
          tmpa+='<span STYLE="FONT-SIZE:20PX;color:#1c2d3f">'+xyz.title+'</span></time>'
          tmpa+='<div class="cbp_tmicon cbp_tmicon-screen"></div>'
          tmpa+='<div class="cbp_tmlabel" style="background:#1c2d3f;">'
          tmpa+='<h2>'+xyz.subtitle+'</h2>'
          tmpa+='<p >'+xyz.content+'</p></div>'
        }

          else
         {           tmpa='<div class="cbp_tmicon cbp_tmicon-screen"></div>'
          tmpa+='<div class="cbp_tmlabel" style="background:#1c2d3f;">'
          tmpa+='<h2>'+xyz.subtitle+'</h2>'

          tmpa+='<p >'+xyz.content+'</p></div>'

        }
          
          document.getElementById("announcement_data").innerHTML+=tmpa;
      }
          document.getElementById("announcement_data").innerHTML+='</li>'

//                document.getElementById("notice_marquee").innerHTML+='</ul>';

    }
  }}

request2.open('GET', '/announcement_get', true);
request2.send();
