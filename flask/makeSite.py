from zipfile import ZipFile 

def makeSite(info):
    fo = open("static/index.html", "w")
    a = f"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta property="og:site_name" content="{info['name']}" />
    <meta property="og:title" content="{info['name']}" />
    <meta property="og:description" content="{info['desc']}" />
    <meta property="og:image" content="{info['img']}" />
    <meta property="og:type" content="website" />
    <title>{info['name']}</title>
    <link href="styles.css" rel="stylesheet" type="text/css" />
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


  </head>
  <body>
    <br><br><br>
    <p class="center">
      <img src="{info['img']}" style="width: 50%; max-width: 225px">
      <h1 class="center thin" style="font-size: 370%">{info['name']}</h1>
    </p>
    <br>
    <h4 class="center ">{info['school']} Class of {info['year']}</h4>
    <br>
    <h4 class="center thin">computer science student</h4>
    <hr width="70%">
    <div class="flex-container">
      <a href="{info['github']}"><i class="fa fa-github"></i></a>
      <a href="{info['resume']}"> <i class="fa fa-file"></i></a>
      <a href="{info['linkedin']}"><i class="fa fa-linkedin"></i></a>
    </div>
    <br><br><br>
  </body>
</html>"""
    fo.write(a)
    fo.close()
    with ZipFile('static/out.zip','w') as zipped:
        zipped.write('static/index.html')
        zipped.write('static/styles.css')
        zipped.close()