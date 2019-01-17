
    function check(val) {
        if(val == 1){
            document.getElementById('lbpregancy').style.display='';
            document.getElementById('pregancytime').value='';
            var radio = document.getElementById('pregancy0');
            radio.checked = true;
        }else{
            document.getElementById('lbpregancy').style.display='none';
            document.getElementById('lbpregancytime').style.display='none';
            document.getElementById('pregancytime').value='0';
            var radio = document.getElementById('pregancy');
            radio.checked = true;
        }
    }

    function check1(val){
        if(val == 1){
            document.getElementById('lbpregancytime').style.display='';
        }else{
            document.getElementById('lbpregancytime').style.display='none';
            document.getElementById('pregancytime').value='0'
        }
    }

    function bmicalc(){
        $("#tip3").animate({opacity:'1'});
        var temp = $("#bmi");
        temp.delay(2000);
        temp.animate({opacity:'1'});

        var weight = $("#weight").val();
        $("#height").on('input propertychange', function () {
            var height = $(this).val();
            height = height/100;
            var bmi = weight/(height*height);
            bmi = bmi.toFixed(1);
            var temp = $("#bmi");
            temp.html('BMI:'+bmi);
        });


    }

    $(document).ready(function(){
        var temp = $("#age");
        temp.focus(function(){
             $("#tip1").animate({opacity:'1'});
         });
        temp.blur(function () {
            $("#tip1").animate({opacity:'0'});
        });
    });


    $(document).ready(function(){
        var temp = $("#weight");
        temp.focus(function(){
             $("#tip2").animate({opacity:'1'});
         });
        temp.blur(function () {
            $("#tip2").animate({opacity:'0'});
        });
    });


    $(document).ready(function(){
        var temp = $("#height");
        temp.blur(function () {
            $("#bmi").animate({opacity:'0'});
            $("#tip3").animate({opacity:'0'});

        });
    });


    $(document).ready(function(){
        var temp = $("#sugar");
        temp.focus(function(){
             $("#tip4").animate({opacity:'1'});
         });
        temp.blur(function () {
            $("#tip4").animate({opacity:'0'});
        });
    });


    $(document).ready(function(){
        var temp = $("#pressure1");
        temp.focus(function(){
             $("#tip5").animate({opacity:'1'});
         });
        temp.blur(function () {
            $("#tip5").animate({opacity:'0'});
        });
    });


    $(document).ready(function(){
        var temp = $("#insulin");
        temp.focus(function(){
             $("#tip6").animate({opacity:'1'});
         });
        temp.blur(function () {
            $("#tip6").animate({opacity:'0'});
        });
    });

        $(document).ready(function(){
        var temp = $("#skin");
        temp.focus(function(){
             $("#tip7").animate({opacity:'1'});
         });
        temp.blur(function () {
            $("#tip7").animate({opacity:'0'});
        });
    });

            $(document).ready(function(){
        var temp = $("#func");
        temp.focus(function(){
             $("#tip8").animate({opacity:'1'});
         });
        temp.blur(function () {
            $("#tip8").animate({opacity:'0'});
        });
    });
