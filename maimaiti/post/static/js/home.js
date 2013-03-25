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

    $('div.item_pic').hover(
        function(){
            $(this).find('div.item_like_tab').show();
            $(this).find('div.item_save_tab').show();
            $(this).find('div.item_desc').show();
        },
        function(){
            $(this).find('div.item_like_tab').hide();
            $(this).find('div.item_save_tab').hide();
            $(this).find('div.item_desc').hide();
        }
    );


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


});