var lotteryinfo = ""; //转动结束后显示信息
var got_one=""; //是否中奖
var cur_user = ""; //当前用户昵称/账号
var lottery_score = 0; //额外抽奖抵扣积分
var rewardstr = ""; //奖品信息
var lottery={
    index:-1,    //当前转动到哪个位置，起点位置
    count:0,    //总共有多少个位置
    timer:0,    //setTimeout的ID，用clearTimeout清除
    speed:20,    //初始转动速度
    times:0,    //转动次数
    cycle:50,    //转动基本次数：即至少需要转动多少次再进入抽奖环节
    prize:-1,    //中奖位置
    init:function(id){
        if ($("#"+id).find(".lottery-unit").length>0) {
            $lottery = $("#"+id);
            $units = $lottery.find(".lottery-unit");
            this.obj = $lottery;
            this.count = $units.length;
            $lottery.find(".lottery-unit-"+this.index).addClass("active");
        };
    },
    roll:function(){
        var index = this.index;
        var count = this.count;
        var lottery = this.obj;
        $(lottery).find(".lottery-unit-"+index).removeClass("active");
        index += 1;
        if (index>count-1) {
            index = 0;
        };
        $(lottery).find(".lottery-unit-"+index).addClass("active");
        this.index=index;
        return false;
    },
    stop:function(index){
        this.prize=index;
        return false;
    }
};

function roll(){
    lottery.times += 1;
    lottery.roll();//转动过程调用的是lottery的roll方法，这里是第一次调用初始化
    if (lottery.times > lottery.cycle+10 && lottery.prize==lottery.index) {
        clearTimeout(lottery.timer);
        lottery.prize=-1;
        lottery.times=0;
        click=false;
        if(got_one=="True"){
            $('#mymemo').html("本次活动你已经中奖");
            $('#id_rwd_list').append(cur_user+" 获得了 "+ rewardstr);
        }
        alert(lotteryinfo);//转动结束后弹出信息

    }else{
        if (lottery.times<lottery.cycle) {
            lottery.speed -= 10;
        }else if(lottery.times==lottery.cycle) {
            //var index = Math.random()*(lottery.count)|0;
            //lottery.prize = index;        
        }else{
            if (lottery.times > lottery.cycle+10 && ((lottery.prize==0 && lottery.index==7) || lottery.prize==lottery.index+1)) {
                lottery.speed += 110;
            }else{
                lottery.speed += 20;
            }
        }
        if (lottery.speed<40) {
            lottery.speed=40;
        };
        //console.log(lottery.times+'^^^^^^'+lottery.speed+'^^^^^^^'+lottery.prize);
        lottery.timer = setTimeout(roll,lottery.speed);//循环调用
    }
    return false;
}


var click=false;


$(document).ready(function(){

    lottery_score = $('#id_ltry_score').val();
    got_one = $('#id_got_one').val();

    lottery.init('lottery');
    $("#lottery a").click(function(){
        var chance = $('#mychance').text();
        var score = $('#myscore').text();
        var handle = true;

        if(got_one=="True"){
            handle = false;
            alert("本次活动你已经中过奖，不能再抽奖");
        }else{
            if(chance <= 0 && score < Number(lottery_score)){
                handle = false;
            }else if(chance <= 0 && score >= Number(lottery_score)){
                var status = confirm("你今天的抽奖机会已用完，你仍可使用"+lottery_score+"积分额外抽奖一次，是否使用积分?");
                if(status){
                    handle = true;
                }else{
                    handle = false;
                };
                
            }else{
                handle = true;
            }
            
        };

        if(!handle){
            if(got_one!="True"){
            alert("你今天的抽奖机会已用完，明天再来吧");
            };
        }else{
            if (click) {//click控制一次抽奖过程中不能重复点击抽奖按钮，后面的点击不响应
                return false;
            }else{
       	    		$.ajax({
                     type:'GET',
                     url:'/roll/',
                     dataType:'json',
                     //data:{"avatarimg":img,},
                     success:function(data)
                      { 

                        var statu = data['status']
                        var rollnum = data['rollnum'];
                        cur_user = data['cur_username'];
                        got_one = data['has_got_one'];
                        rewardstr = data['rewardstr'];

                        if(statu==0){
                            lotteryinfo="本次活动你已经中过奖，不能再抽奖";
                        }else if(statu==-1){
                            lotteryinfo="你今天的抽奖机会已用完，明天再来吧";
                        }else{
                            //alert(rollnum);
                            lottery.prize=rollnum;

                            if(got_one=="True"){

                                lotteryinfo="恭喜你抽中"+rewardstr
                                $('#id_got_one').val('True');

                            }else{
                                lotteryinfo="你与大奖擦肩而过"
                            }
        
                            lottery.speed=100;
                		    roll();    //转圈过程不响应click事件，会将click置为false
                		    click=true; //一次抽奖完成后，设置click为true，可继续抽奖
                            $('#mychance').text(data['mychance']);
                            $('#myscore').text(data['myscore']);
                		  return false;
                        }
                        
                      },
                     error:function(data)
                     {
                      alert("无法获取抽奖数据,请重试"); 
                     }
                    });
    
    
            };
        };
    });
});