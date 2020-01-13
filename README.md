# super-duper-flask-led-pi-thing
A short demo for IT2 Lesson; How to use Flask to light up LEDs on a PI


# FLASK - REDIRECT TO INDEX.html
```python
@app.route('/')
def index_redirect():
    return redirect("/static/index.html", code=302)
```


# FLASK - API - ButtonStatus

```python
@app.route('/api/status', methods=['get'])
def api_status():
    global wiringpi
    status = {}
    status['button_yellow'] = True
    status['button_blue'] = False
    return jsonify(status)
```

# HTML - IMAGES FOR BUTTON
```html
<table>
  <tr>
    <td><img src="img/btn_yellow_released.png" id="btn_yellow_img" /></td><!-- 4 -->
    <td><img src="img/btn_blue_released.png" id="btn_blue_img" /></td><!-- 4 -->
  </tr>
</table>
```

# JS- GET BUTTON STATE FROM API
```js
 $.get( "/api/status", function( data ) {
      console.log(data);
      
      //----6 ----/*
      if(data.button_yellow){
        $("#btn_yellow_img").attr("src","img/btn_yellow_pressed.png");
      }else{
        $("#btn_yellow_img").attr("src","img/btn_yellow_released.png");
      }

      //----7 ----/*
      if(data.button_blue){
        $("#btn_blue_img").attr("src","img/btn_blue_pressed.png");
      }else{
        $("#btn_blue_img").attr("src","img/btn_blue_released.png");
      }

    });
```
