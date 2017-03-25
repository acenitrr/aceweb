var request = new XMLHttpRequest();

request.onreadystatechange = function(response) {
  if (request.readyState === 4) {
    if (request.status === 200) {

      var ProfileJsonList = JSON.parse(request.responseText);

            document.getElementById("profile").innerHTML=ProfileJsonList['list'];
      // for(var x=0;x<ProfileJsonList['list'].length;x++)
      // {

      //     document.getElementById("profile").innerHTML+= ProfileJsonList;
      // }
//                document.getElementById("notice_marquee").innerHTML+='</ul>';

    }
  }}

request.open('GET', '/profile_get', true);
request.send();