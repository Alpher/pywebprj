$(function() {
    var signFun = function() {

        var dateArray = []; // 假设已经签到的从0开始

       $.ajax({
                 type:'GET',
                 url:'/getchkinday/',
                 dataType:'html',
                 //data:{"avatarimg":img,},
                 success:function(data)
                  { 
                    var strs = data.split(',')
                    for (i=0;i<strs.length ;i++ ) { 
                            dateArray[i]=Number(strs[i]-1)
                    };
                    for (var i = 0; i < totalDay; i++) {
                        $dateLi.eq(i + monthFirst).addClass("date" + parseInt(i + 1));
                        for (var j = 0; j < dateArray.length; j++) {
                            if (i == dateArray[j]) {
                                $dateLi.eq(i + monthFirst).addClass("qiandao");
                            }
                        }
                    } //生成当月的日历且含已签到
                    
                  },
                 error:function(data)
                 {
                  alert("加载签到日历数据失败，请刷新页面"); 
                 }
                });

                    var $dateBox = $("#js-qiandao-list"),
                        $currentDate = $(".current-date"),
                        $qiandaoBnt = $("#js-just-qiandao"),
                        _html = '',
                        _handle = Boolean(parseInt($("#handle_chk").val())),
                        myDate = new Date();
                    $currentDate.text(myDate.getFullYear() + '年' + parseInt(myDate.getMonth() + 1) + '月' + myDate.getDate() + '日');
            
                    var monthFirst = new Date(myDate.getFullYear(), parseInt(myDate.getMonth()), 1).getDay();
            
                    var d = new Date(myDate.getFullYear(), parseInt(myDate.getMonth() + 1), 0);
                    var totalDay = d.getDate(); //获取当前月的天数

                    for (var i = 0; i < 42; i++) {
                        _html += ' <li><div class="qiandao-icon"></div></li>'
                    }
                    $dateBox.html(_html) //生成日历网格
            
                    var $dateLi = $dateBox.find("li");
                    for (var i = 0; i < totalDay; i++) {
                        $dateLi.eq(i + monthFirst).addClass("date" + parseInt(i + 1));
                        for (var j = 0; j < dateArray.length; j++) {
                            if (i == dateArray[j]) {
                                $dateLi.eq(i + monthFirst).addClass("qiandao");
                            }
                        }
                    } //生成当月的日历且含已签到
            
                    $(".date" + myDate.getDate()).addClass('able-qiandao');
                    //判断是否曾经签到
                    if (_handle==false){
                        $qiandaoBnt.addClass('actived');
                    };

        // $dateBox.on("click", "li", function() {
        //         if ($(this).hasClass('able-qiandao') && _handle) {
        //             $(this).addClass('qiandao');
        //             qiandaoFun();
        //         }
        //     }) //签到

        $qiandaoBnt.on("click", function() {
            if (_handle) {
                qiandaoFun();
            }
        }); //签到

        function qiandaoFun() {

        //
        $.ajax({
                 type:'GET',
                 url:'/checkin/',
                 dataType:'json',
                 //data:{"avatarimg":img,},
                 success:function(data)
                  { 
                    $.each(data,function(i,n){
                        $("#"+i).html(n)
                    });
                    $qiandaoBnt.addClass('actived');
                    openLayer("qiandao-active", qianDao);
                    _handle = false;
                  },
                 error:function(data)
                 {
                  alert("签到失败，请重试"); 
                 }
                });


        }

        function qianDao() {
            $(".date" + myDate.getDate()).addClass('qiandao');
        }
    }();

    function openLayer(a, Fun) {
        $('.' + a).fadeIn(Fun)
    } //打开弹窗

    var closeLayer = function() {
            $("body").on("click", ".close-qiandao-layer", function() {
                $(this).parents(".qiandao-layer").fadeOut()
            })
        }() //关闭弹窗

    $("#js-qiandao-history").on("click", function() {
        //获取个人签到统计数据
        $.ajax({
                 type:'GET',
                 url:'/getchkinov/',
                 dataType:'json',
                 //data:{"avatarimg":img,},
                 success:function(data)
                  { 
                    $.each(data,function(i,n){
                        $("#"+i).html(n)
                    });
                    openLayer("qiandao-history-layer");
                  },
                 error:function(data)
                 {
                  alert("获取签到统计数据失败，请重试"); 
                 }
                });

    })

})
