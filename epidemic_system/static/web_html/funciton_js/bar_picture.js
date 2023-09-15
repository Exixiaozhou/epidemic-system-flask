function bar_option_fun(ECharts){
    ECharts.showLoading()
    var optionBar = {
        animation:true, //配置动画是否开启
        animationDuration:5000, //配置动画时长，单位毫秒
        dataZoom: [{
            type:'slider', //x轴下方拖动进行图表缩放显示
            type:'inside', // 通过滚轮进行图标缩放显示
            xAxisIndex:0
        }, {
            type: 'inside', //x轴下方拖动进行图表缩放显示
        }],
        title:{
            text: "现有确诊数排名前十地区",
            font_family: "楷体",
            left: 0,
            top: 0,
            textStyle:{
                color: '#FF1493',
                fontSize : '18',
                fontFamily: "楷体",
                color: 'white'
            }
        },
        tooltip:{
            trigger: 'axis', // 设置 触碰x轴则生效
        },
        legend:{
            top: 25,
            data: ['现有确诊'],
            left : 'center',
            textStyle: {
                fontSize: 15,
                fontFamily: "楷体"
            }
        },
        xAxis:{
            data: [],
            boundaryGap: 'false' //配置false 折线图紧挨边缘,
        },
        yAxis: {
            type:'value',
            axisLabel: {
                show: true,
                fontSize: 12,
                formatter: function (value){
                    if (value>=1000){
                        value = value / 1000 + 'k'
                    }
                    return value
                }
            }
        },
        series: [
            {
                type: 'bar',
                name: '现有确诊',
                width: 0,
                color: '#F8F8FF',
                data: [],
                stack: 'total',
                label: {
                    show: true, //显示x轴的数据
                    position: 'top' //设置在顶端显示
                },
            },
            // {
            //     type: 'bar',
            //     name: '死亡',
            //     width: 0,
            //     color: '#FF0000',
            //     data: [],
            // }
        ]
    };
    ECharts.hideLoading()
    return optionBar
}

var bar_echarts = echarts.init(document.querySelector('#bar'), "dark");
var bar_options = bar_option_fun(bar_echarts)
bar_echarts.setOption(bar_options)

