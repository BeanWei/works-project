$.getJSON("./jsonData/data.json", function (data) {
    var selected = {};
    for (var i in data) {
        selected[data[i].name] = true;
    }
    var myChart = echarts.init(document.getElementById("showAllBox"));
    myChart.setOption(option = {
        //标题
        title: {
            text: 'Bean.Wei',
            subtext: 'demo test'
        },
        tooltip: {
            trigger: 'axis'
        },
        //图例名
        legend: {
            show: false,
        },
        grid: {
            //top: '10%',
            left: '3%',   //图表距边框的距离
            right: '150',
            bottom: '10%',
            containLabel: true
        },
        //工具框，可以选择
        toolbox: {
            x:'center',
            itemGap: 20,
            feature: {
                dataZoom: {},
                dataView: {
                    readOnly: false, 
                    optionToContent: function(opt) {
                        var axisData = opt.xAxis[0].data;
                        var series = opt.series;
                        var table = '<table class="layui-table" lay-even="" lay-skin="row"><tbody><tr>'
                                     + '<td>SN</td>'
                                     + '<td>12-01</td>'
                                     + '<td>12-02</td>'
                                     + '<td>12-03</td>'
                                     + '<td>12-04</td>'
                                     + '<td>12-05</td>'
                                     + '<td>12-06</td>'
                                     + '<td>12-07</td>'
                                     + '<td>12-08</td>'
                                     + '<td>12-09</td>'
                                     + '<td>12-010</td>'
                                     + '<td>12-011</td>'
                                     + '<td>12-012</td>'
                                     + '<td>12-013</td>'
                                     + '</tr>';
                        for (var i = 0, l = series.length; i < l; i++) {
                            table += '<tr>'
                                     + '<td>' + series[i].name + '</td>'
                                     + '<td>' + series[i].data[1] + '</td>'
                                     + '<td>' + series[i].data[2] + '</td>'
                                     + '<td>' + series[i].data[3] + '</td>'
                                     + '<td>' + series[i].data[4] + '</td>'
                                     + '<td>' + series[i].data[5] + '</td>'
                                     + '<td>' + series[i].data[6] + '</td>'
                                     + '<td>' + series[i].data[7] + '</td>'
                                     + '<td>' + series[i].data[8] + '</td>'
                                     + '<td>' + series[i].data[9] + '</td>'
                                     + '<td>' + series[i].data[10] + '</td>'
                                     + '<td>' + series[i].data[11] + '</td>'
                                     + '<td>' + series[i].data[12] + '</td>'
                                     + '<td>' + series[i].data[13] + '</td>'
                                     + '</tr>';
                        }
                        table += '</tbody></table>';
                        return table;
                    }
                },
                restore: {},
                saveAsImage: {},
            }
        },
        //x轴范围滑动
        calculable : true,
        dataZoom : {
            show : true,
            realtime : true,
            start : 0,
            end : 100
        },
        //x轴信息样式
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['12-01','12-02','12-03','12-04','12-05','12-05','12-06','12-07','12-08','12-09','12-10','12-11','12-12','12-13'],
            //坐标轴颜色
            axisLine:{
                lineStyle:{
                    color:'red'
                }
            },
            //x轴文字旋转
            axisLabel:{
                rotate:30,
                interval:0
            },
        },

        yAxis : [
            {
                type : 'value',
                axisLabel : {
                    formatter: '{value} 人'
                }
            }
        ],
        series: data.map(function(item){
            return {
                name: item.name,
                type: item.type,
                symbol: item.symbol,
                symbolSize: item.symbolSize,
                itemStyle: {
                    normal: {
                        color: item.itemStyle.normal.color,
                        borderColor: item.itemStyle.normal.borderColor
                    }
                },
                data: item.data.map(function(value) {
                    return value
                })
            }
        })
    })
})
