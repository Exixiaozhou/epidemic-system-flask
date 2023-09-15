function line_option_fun(ECharts){
    ECharts.showLoading()
    var optionLine = {
         animation:true, //配置动画是否开启
        animationDuration:5000, //配置动画时长，单位毫秒
        title:{
            text: "全国疫情趋势",
            font_family: "楷体",
            left: 10,
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
            left: 'right',
            data: ['累计确诊', '现有确诊', '累计治愈','累计死亡'],
            left : 'center',
            textStyle: {
                fontSize: 15,
                fontFamily: "楷体"
            }
        },
        xAxis:{
            type: 'category',
            data: [],
            boundaryGap: 'false' //配置false 折线图紧挨边缘,
        },
        yAxis:{
            'type': 'value',
            scale: 'true',  //配置y轴的值不是从0开始，从y轴的最小值开始
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
        dataZoom:[
            {
              type: 'inside'
            }
        ],
        series: [
            {
                type: 'line',
                name: '累计确诊',
                color: '#00FFFF',
                stack : 'prices',
                data: []
            },
            {
                type: 'line',
                name: '现有确诊',
                color: '#00BFFF',
                stack : 'prices',
                data: []
            },
            {
                type: 'line',
                name: '累计治愈',
                color: '#00FF00',
                stack : 'prices',
                data: []
            },
                        {
                type: 'line',
                name: '累计死亡',
                color:'#0000FF',
                stack : 'prices',
                data: []
            },
        ]
    };
    ECharts.hideLoading()
    return optionLine
}

var line_echarts = echarts.init(document.querySelector('#line'), "dark");
var line_options = line_option_fun(line_echarts)
line_echarts.setOption(line_options)
