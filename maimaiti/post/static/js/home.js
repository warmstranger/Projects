/**
 * Created with PyCharm.
 * User: egibbon
 * Date: 13-3-19
 * Time: 下午1:53
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function(){
//    $("#category").Scroller({
//        next:"arrow_next",
//        prev:"arrow_prev",
//        frame:"category_frame",
//        child:"category_pics",
//        num:"showNum",
//        time :4000,
//        auto:true
//    });
    $('input').bind('focus',function(){
        $(this).siblings('label').css('opacity',$.trim(this.value)=='' ? 0.5 : 0);
        }).bind('keydown',function(){
        $(this).siblings('label').css('opacity',0);
        }).bind('blur',function(){
        $(this).siblings('label').css('opacity',$.trim(this.value)=='' ? 1 : 0)
        });

//    home1.html
//    $('div.item_pic').hover(
//        function(){
//            $(this).find('div.item_like_tab').show();
//            $(this).find('div.item_save_tab').show();
//            $(this).find('div.item_desc').show();
//        },
//        function(){
//            $(this).find('div.item_like_tab').hide();
//            $(this).find('div.item_save_tab').hide();
//            $(this).find('div.item_desc').hide();
//        }
//    );
//    home2.html
    $('div.item_pic').hover(
        function(){
            $(this).find('div.item_hover_tab').show();
        },
        function(){
            $(this).find('div.item_hover_tab').hide();
        }
    );
//    alert($('div.item_pic').length);


    $('#pic_slide').nivoSlider();

    $('#category_frame').carouFredSel({
        auto: false,
        prev: '#arrow_prev',
        next: '#arrow_next',
        pagination: "#pager2",
        mousewheel: false,
        swipe: {
            onMouse: false,
            onTouch: true
        }
    });

    $(".head_btn_trans").click(function(){
        var collection= $(this);
        var postId = collection.attr("id");
        if(collection.text() =="收藏")
        {
            $.ajax({
                type:"GET",
                url: "/collection/collect/"+postId,
                cache:false,
                dataType:"json",
                success:function(data){
                    $("div.modal").modal('show');
                    $(".modal-body").find('p').html('');
                    $(".modal-body").find('p').append(data.msg);
                    if(data.flag!=-1)
                        collection.text("取消收藏");
                }
            });
        }
        else
        {
            $.ajax({
                type:"GET",
                url: "/collection/cancel_collect/"+postId,
                cache:false,
                dataType:"json",
                success:function(data){
                    $("div.modal").modal('show');
                    $(".modal-body").find('p').html('');
                    $(".modal-body").find('p').append(data.msg);
                    if (data.flag!=-1)
                        collection.text("收藏");
                }
            });
        }
    });


    $('.btn btn-primary').click(function(){
        alert("aaa");
        $("div.modal").modal('hide');
        });

    function closeDL(){
        $("div.modal").modal('hide');

        }
});

    //follow


