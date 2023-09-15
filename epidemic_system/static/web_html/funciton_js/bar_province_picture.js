function bar_province_fun(ECharts){
     ECharts.showLoading()
     var bar_province_option = {
          animation:true, //配置动画是否开启
          animationDuration:5000, //配置动画时长，单位毫秒
          title:{
               text: "",
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
               data: ['累计确诊'],
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
                    type:'slider', //x轴下方拖动进行图表缩放显示
                    type:'inside', // 通过滚轮进行图标缩放显示
                    xAxisIndex:0
               }
          ],
          series: [
               {
                    type: 'bar',
                    name: '累计确诊',
                    color: '#00BFFF',
                    stack : 'prices',
                    data: [],
                    stack: 'total',
                    label: {
                    show: true, //显示x轴的数据
                    position: 'top' //设置在顶端显示
                },
               }
         ]

     };
     ECharts.hideLoading()
     return bar_province_option
}

var bar_province_echarts = echarts.init(document.querySelector('#line2'), "dark");
var bar_province_options = bar_province_fun(bar_province_echarts)
bar_province_echarts.setOption(bar_province_options)

