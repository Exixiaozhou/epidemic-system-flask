function get_times(){
    $.ajax({
        type: "get",
        url: "http://localhost:8888/get_data/get_times",
        datatype: 'json',
        success: function (times){
            $("#times").html(times)
        },
        error: function () {
            alert('请求获取当前时间接口失败!')
        }
    });
 }
setInterval(get_times, 500)

function get_label_number(){
    $.ajax({
        type : 'get',
        url: "http://localhost:8888/get_data/get_label_data",
        datatype : "json",
        success: function (data){
            $(".number h1").eq(0).html(data['diagnosed'])
            $(".number h1").eq(1).html(data['current_confirmed_count'])
            $(".number h1").eq(2).html(data['cured'])
            $(".number h1").eq(3).html(data['death'])
        },
        error: function () {
            alert('请求全国疫情统计数据失败!')
        }
    })
}
setInterval(get_label_number, 1000*10)

function get_line_data(){
    $.ajax({
        type : 'get',
        url: "http://localhost:8888/get_data/get_line_data",
        datatype : "json",
        success: function (data){
            line_options.xAxis.data = data['times_list']
            line_options.series[0].data= data['diagnosed_list']
            line_options.series[0].color= data['color_list'][0]
            line_options.series[1].data= data['current_confirmed_count_list']
            line_options.series[1].color= data['color_list'][1]
            line_options.series[2].data= data['cured_list']
            line_options.series[2].color= data['color_list'][2]
            line_options.series[3].data= data['death_list']
            line_options.series[3].color= data['color_list'][3]
            line_echarts.setOption(line_options)
        },
        error: function () {
            alert('请求全国疫情统计数据失败!')
        }
    })
}
setInterval(get_line_data, 1000*10)

function get_bar_data(){
    $.ajax({
        type : 'get',
        url: "http://localhost:8888/get_data/get_bar_data",
        datatype : "json",
        success: function (data){
            bar_options.xAxis.data = data['province_name_list']
            // bar_options.series[0].data = data['dead_count_list']
            bar_options.series[0].data = data['current_confirmed_count_list']
            bar_options.series[0].color = data['color_list'][0]
            bar_echarts.setOption(bar_options)
        },
        error: function () {
            alert('请求各城市疫情数据分布失败!')
        }
    })
}
setInterval(get_bar_data, 1000*10)

function get_pie_data(){
     $.ajax({
        type : 'get',
        url: "http://localhost:8888/get_data/get_pie_data",
        datatype : "json",
        success: function (data){
            pie_option.series[0].data = data['data_list']
            pie_option.series[0].color = data['color_list']
            pie_echarts.setOption(pie_option)
        },
        error: function () {
            alert('请求国外疫情数据分布失败!')
        }
    })
}
setInterval(get_pie_data, 1000*10)

function get_bar_province_data(){
    $.ajax({
        type : 'get',
        url: "http://localhost:8888/get_data/get_province_data",
        datatype : "json",
        success: function (data){
            console.log(data)
            bar_province_options.title.text = data['province_name'] + '区域详细数据分布'
            bar_province_options.xAxis.data = data['province_name_list']
            bar_province_options.series[0].data = data['confirmed_count_list']
            bar_province_options.series[0].color = data['color_list'][0]
            bar_province_echarts.setOption(bar_province_options)
        },
        error: function () {
            alert('请求各省份区域疫情数据分布失败!')
        }
    })
}
setInterval(get_bar_province_data, 1000*10)

function get_map_data(){
    $.ajax({
        type : 'get',
        url: "http://localhost:8888/get_data/get_map_data",
        datatype : "json",
        success: function (data){
            map_option.series[0].data = data
            map_echarts.setOption(map_option)
        },
        error: function () {
            alert('请求全国疫情数据分布失败!-地图')
        }
    })
}

setInterval(get_map_data, 1000*10)

get_times()
get_label_number()
get_line_data()
get_bar_data()
get_pie_data()
get_bar_province_data()
get_map_data()
