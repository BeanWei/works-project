<template>
    <div id="linechart">
        <el-row>
            <el-col :span="4">
                <el-row>
                    <el-cascader
                        placeholder="添加Limit(可搜索)"
                        style="width: 160px"
                        :options="limitoptions"
                        filterable
                        @change="getLimitData">
                    </el-cascader>
                    <el-button type="primary" icon="el-icon-edit" circle @click="dialogLimitFormVisible = true"></el-button>
                </el-row>
            </el-col>
            <el-col :span="20">
                <el-slider
                    v-model="yValueRange"
                    range
                    :min="-1000"
                    :max="1000"
                    @change="filterY">
                </el-slider>
            </el-col>
        </el-row>
        <el-row :gutter="2">
            <el-col :span="15">
                <div id="chart"></div>
                <div id="hoverinfo" style="margin-left: 80px;"></div>
            </el-col>
            <el-col :span="8" v-if="show">
                <div style="text-align: center;">
                    <el-transfer
                        style="text-align: left; display: inline-block"
                        v-model="tagindex"
                        filterable
                        :titles="['Source', 'Target']"
                        :format="{
                            noChecked: '${total}',
                            hasChecked: '${checked}/${total}'
                        }"
                        :data="itemnames">
                        <span class="transferfooter" slot="left-footer" style="color:rgb(150,150,150);size:12;">Tips: 选中数据进行更多操作</span>
                        <el-dropdown class="transferfooter" slot="right-footer" @command="handleCommand">
                            <span class="el-dropdown-link">
                                工具栏<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="delTargetData">删除目标数据</el-dropdown-item>
                            <el-dropdown-item command="changeLineColor">调整曲线颜色</el-dropdown-item>
                        </el-dropdown-menu>
                        </el-dropdown>
                    </el-transfer>
                </div>
            </el-col>
        </el-row>

        <!-- limit 数据添加对话框表单 -->
        <el-dialog title="添加Limit数据" :visible.sync="dialogLimitFormVisible" append-to-body width="50%">
            <el-form ref="limitform" :model="limitform" :rules="rules" label-width="100px">
                <el-form-item label="机种名称" prop="projectname">
                    <el-input v-model="limitform.projectname"></el-input>
                </el-form-item>
                <el-form-item label="Limit名称" prop="limitname">
                    <el-input v-model="limitform.limitname"></el-input>
                </el-form-item>
                <el-form-item label="X轴数据" prop="xdata">
                    <el-input type="textarea" v-model="limitform.xdata"></el-input>
                </el-form-item>
                <el-form-item label="Y轴数据" prop="ydata">
                    <el-input type="textarea" v-model="limitform.ydata"></el-input>
                </el-form-item>
                <el-form-item label="Smooth">
                    <el-switch active-color="#13ce66" v-model="limitform.limitsmoothbool"></el-switch>
                </el-form-item>
                <el-form-item>
                    <el-button @click="dialogLimitFormVisible = false">取 消</el-button>
                    <el-button type="primary" @click="addLimit('limitform')">确 定</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>

        <!-- 曲线颜色选择对话框表单 -->
        <el-dialog title="曲线颜色选择器" :visible.sync="dialogcolorFormVisible" append-to-body width="30%">
            <el-form>
                <el-form-item label="颜色选择">
                    <div class="block">
                        <el-color-picker v-model="linecolorvalue"></el-color-picker>
                    </div>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogcolorFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="changeLineColor">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import Plotly from 'plotly.js-dist/plotly.js';
import { setTimeout, setInterval } from 'timers';
import { changeStr2Float } from '../../assets/js/utils.js';
//import { ipcRenderer } from 'electron';
export default {
    name: "linechart",
    props: {
        dataset: {
            type: Array,
            default: null
        },
        tmpdataset: {
            type: Array,
            default: null
        },
        YrangeDict: {
            type: Object,
            default: null
        }
    },
    data: function() {
        return {
            // loading the limit
            limitoptions: [],
            selectedOptions: [],
            // edit/add the limit
            limitform: {
                projectname: '',
                limitname: '',
                xdata: '',
                ydata: '',
                limitsmoothbool: false
            },
            rules: {
                projectname: [
                    {required: true, message: '请输入项目名称', trigger: 'blur'}
                ],
                limitname: [
                    {required: true, message: '请输入Limit名称', trigger: 'blur'}
                ],
                xdata: [
                    {required: true, message: '请输入X轴数据', trigger: 'blur'}
                ],
                ydata: [
                    {required: true, message: '请输入Y轴数据', trigger: 'blur'}
                ]
            },

            // all the test data 
            TRACES: [],

            // INIT MOCK DATA
            MOCKDATA: [
                {
                    //"x": [100.00,106.00,112.00,118.00,125.00,132.00,140.00,150.00,160.00,170.00,180.00,190.00,200.00,212.00,224.00,236.00,250.00,265.00,280.00,300.00,315.00,335.00,355.00,375.00,400.00,425.00,450.00,475.00,500.00,530.00,560.00,600.00,630.00,670.00,710.00,750.00,800.00,850.00,900.00,950.00,1000.00,1060.00,1120.00,1180.00,1250.00,1320.00,1400.00,1500.00,1600.00,1700.00,1800.00,1900.00,2000.00,2120.00,2240.00,2360.00,2500.00,2650.00,2800.00,3000.00,3150.00,3350.00,3550.00,3750.00,4000.00,4250.00,4500.00,4750.00,5000.00,5300.00,5600.00,6000.00,6300.00,6700.00,7100.00,7500.00,8000.00,8500.00,9000.00,9500.00,10000.00,10600.00,11200.00,11800.00,12500.00,13200.00,14000.00,15000.00,16000.00,17000.00,18000.00,19000.00,20000.00],
                    //"y": [9.37,13.92,19.14,26.57,37.45,42.30,36.30,21.98,12.63,7.08,4.28,2.81,1.89,1.24,0.83,0.60,0.44,0.31,0.24,0.21,0.18,0.19,0.21,0.22,0.22,0.21,0.20,0.24,0.29,0.29,0.30,0.30,0.40,0.38,0.33,0.40,0.40,0.39,0.44,0.38,0.42,0.73,1.03,0.67,0.72,0.57,0.74,0.46,0.50,0.54,0.62,1.22,1.34,0.74,0.39,0.49,0.65,0.74,0.84,0.70,0.57,0.39,0.82,1.23,1.36,2.65,6.07,3.44,3.35,3.27,1.33,1.57,1.81,2.03,3.53,0.37,1.24,0.76,0.79,0.40,0.26,0.13,0.57,0.36,0.53,0.62,0.69,0.44,0.36,0.24,0.23,0.20,0.42],
                    "x": [],
                    "y": [],
                    "type": "scatter",
                    "mode": "lines",
                    "name": "",
                    "line": {
                        "color": "#40C6FF",
                        "shape": "linear",
                        "width": 1
                    }
                }
            ],

            itemnames: [],
            tagindex: [],

            dialogcolorFormVisible: false,
            linecolorvalue: "#409EFF",
            dialogLimitFormVisible: false,

            // if show the right control area(when the windows size is change)
            show: true,
            theInitHeight: 0,

            //Y yaxis range selecte
            yValueRange: [-1000, 1000],
        }
    },
    mounted() {
        // 调整因窗口大小变化的页面布局
        this.theInitHeight = parseInt(document.documentElement.clientHeight);
        const that = this;
        window.onresize = function windowResize() {
            var theHeight = parseInt(document.documentElement.clientHeight);
            if ((that.theInitHeight - theHeight) > that.theInitHeight/16) {
                that.show = false;
            } else {
                that.show = true;
            }
        },

        //更新Mock数据来初始化界面.
        this.Update(this.MOCKDATA);

        // 从本地config.json文件加载limit数据
        this.$electron.ipcRenderer.send('GetConfig');
        this.$electron.ipcRenderer.on('GetConfigReply', (event, data) => {
            if (Object.keys(data).length === 0) {
                this.openNotice("error", "Limit数据为空")
            } else {
                var projects = [];
                for (var key in data.projects) {
                    projects.push(key);
                };
                projects.forEach((projectname, _) => {
                    var op = {};
                    var childitems = [];
                    for (var key in data.projects[projectname]) {
                        var childoption = {};
                        childoption.label = key;
                        childoption.value = data.projects[projectname][key];
                        childitems.push(childoption);
                    };
                    op.value = projectname;
                    op.label = projectname;
                    op.children = childitems;
                    this.limitoptions.push(op);
                });
                this.openNotice("success", "成功加载Limit数据")
            }
        });

    },
    methods: {
         // 打开提示，常用于主动操作后的反馈提示。与 Notification 的区别是后者更多用于系统级通知的被动提醒。
        openNotice(type, text) {
            if (type === "alert") {
                //普通提示
                this.$message(text);
            } else if (type === "info") {
                // 成功的提示
                this.$message({
                message: text,
                type: "info",
                duration: 1000,
                });
            } else if (type === "success") {
                // 成功的提示
                this.$message({
                message: text,
                type: "success",
                duration: 1000,
                });
            } else if (type === "warning") {
                // 提出警告
                this.$message({
                message: text,
                type: "warning",
                duration: 1000,
                });
            } else if (type === "error") {
                // error  错误提示
                this.$message({
                message: text,
                type: "error",
                duration: 1000,
                });
            } else {
                //普通提示
                this.$message(text);
            }
        },
        Update(thetrace) {
            this.TRACES = thetrace;
            var layout = {
                showlegend: false,
                hovermode: 'closest',
                height: 360,
                margin: {
                    l: 24,
                    r: 10,
                    t: 10,
                    b: 20
                },
                xaxis: {
                    type: 'log',
                    // tickmode: 'linear',
                    // tick0: '0, 100,',
                    // dtick: '1000',
                    //tickformat: '10^',
                    showgrid: true, 
                    zeroline: false,
                    //showticklabels: true,
                },
                yaxis: {
                    //title: '', 
                    showline: true,
                    showgrid: true,
                }
            };
            
            Plotly.newPlot("chart", this.TRACES, layout, {displaylogo: false})

            var hoverinfo = document.getElementById("hoverinfo")
            var thechart = document.getElementById("chart")

            // 鼠标悬停提示信息
            var data = this.TRACES;
            thechart.on('plotly_hover', function(data) {
                var infotext = data.points.map(function(d){
                    return (d.data.name+': x= '+d.x+',y= '+d.y.toPrecision(3))
                })
                hoverinfo.innerHTML = infotext.join('<br/>')
            }).on('plotly_unhover', function(data) {
                hoverinfo.innerHTML = ""
            })

            // 曲线点击标注
            // TODO: BUG--> 当X轴数据类型设置为log时，这个功能则会失效...
            var annotations = [];
            thechart.on('plotly_click', function(data) {
                for(var i = 0; i < data.points.length; i++) {
                    var annotate_text = 'x = '+data.points[i].x +
                                    ' y = '+data.points[i].y.toPrecision(4); 
                    // 利用横坐标相等则移除的方法来实现反选
                    var isExist = false;
                    var existIndex = -1;
                    for (var index = 0; index < annotations.length; index++){
                        if (annotations[index].x === data.points[i].x) {
                            isExist = true;
                            existIndex = index;
                            break;
                        }
                    };                           
                    if (isExist) {
                        annotations.splice(existIndex, 1)
                    } else {
                        var annotation = {
                            text: annotate_text,
                            x: data.points[i].x,
                            y: parseFloat(data.points[i].y.toPrecision(4))
                        }
                        annotations.push(annotation);
                    }               
                    Plotly.relayout("chart", {annotations: annotations})
                }
            })

            //更新右侧操作区域数据
            this.itemnames = [];
            this.tagindex = [];
            this.TRACES.forEach((trace, index) => {
                if (trace.y.length !== 0) {
                    this.itemnames.push({
                        label: trace.name,
                        key: index
                    });
                }
            });
            this.openNotice("info", "数据已更新");
            //this.$message.info("数据已更新")
        },
        handleCommand(command) {
            if (command === "changeLineColor") {
                if (this.tagindex.length === 0) {
                    this.openNotice("warning", "请先选择要调整颜色的曲线!");
                } else {
                    this.dialogcolorFormVisible = true
                }
            } else if (command === "delTargetData") {
                if (this.tagindex.length === 0) {
                    this.openNotice("warning", "请先选择要删除的数据!");
                } else {
                    this.$confirm('此操作将移除选中数据在曲线图中的显示, 是否继续?', '提示', {
                        confirmButtonText: '确定',
                        cancelButtonText: '取消',
                        type: 'warning'
                    }).then(() => {
                        this.tagindex.forEach((key, _) => {
                            delete this.TRACES[key]                      
                        });
                        for ( var i = this.TRACES.length-1; i >= 0; i--) {
                            if (this.TRACES[i] === undefined) {
                                this.TRACES.splice(i, 1);
                            }
                        };
                        this.Update(this.TRACES);
                        this.openNotice("success", "数据删除成功!");
                    }).catch(() => {
                        this.openNotice("info", "已取消删除!");
                    })
                }
            }
        },
        changeLineColor() {
            this.dialogcolorFormVisible = false
                this.tagindex.forEach((key, index) => {
                    this.TRACES[key]["line"]["color"] = this.linecolorvalue
                });
                this.Update(this.TRACES);
                this.openNotice("success", "曲线颜色更新成功");
        },
        // 选择Limit数据添加到所有曲线数据中
        getLimitData(val) {
            // limit选择层级只有两层 Project -> LimitData.
            // 这里的val是一个数组，Arr[0]是第一级，Arr[1]是第二级，以此类推。
            var selData = val[1]
            // 检查数据，禁止重复添加
            for (var i = 0; i < this.TRACES.length; i++) {
                if(this.TRACES[i] === selData) {
                    this.openNotice("warning", "勿重复添加Limit！");
                    return
                }
            }
            this.TRACES.push(selData);
            this.Update(this.TRACES);
        },
        // 添加/编辑Limit数据到本地
        addLimit(limitform) {
            this.$refs[limitform].validate((valid) => {
                if (valid) {
                    // 将str格式的x/y数据转为数组
                    var Xdata = [];
                    var Ydata = [];
                    var _xdata = this.limitform.xdata.split(',');
                    var _ydata = this.limitform.ydata.split(',');
                    for (var xi = 0; xi < _xdata.length; xi++) {
                        Xdata.push(changeStr2Float(_xdata[xi]))
                    };
                    for (var yi = 0; yi < _ydata.length; yi++) {
                        Ydata.push(changeStr2Float(_ydata[yi]))
                    };
                    var lineshapetype = "linear";
                    if (this.limitform.limitsmoothbool) {
                        lineshapetype = "spline"
                    };
                    var cfgObj = {
                        "projectname": this.limitform.projectname,
                        "limitname": this.limitform.limitname,
                        "Xdata": Xdata,
                        "Ydata": Ydata,
                        "lineshapetype": lineshapetype
                    };
                    // 添加/编辑 limit数据保存于本地config.json
                    this.$electron.ipcRenderer.send('SetConfig', cfgObj);
                    this.dialogLimitFormVisible = false;
                    this.$electron.ipcRenderer.on('SetConfigReply', (event, msg) => {
                        this.openNotice("info", msg);
                    });
                }
            })
        },
        // 从父组件获取数据源
        getYrangeDictfromParent(dic, tmp) {
            this.theRangeDic = dic;
            this.tmpTRACES = tmp;
        },
        // Y轴滑块范围，以此筛选曲线
        filterY(rangeVal) {
            var newTrace = [];
            for (var key in this.theRangeDic) {
                if (rangeVal[0]<this.theRangeDic[key][0] && rangeVal[1]>this.theRangeDic[key][1]) {
                    if (this.tmpTRACES[key] === undefined) {
                        console.log(this.tmpTRACES.length);
                    }
                    newTrace.push(this.tmpTRACES[key])
                }
            };
            //console.log(newTrace)
            this.Update(newTrace);
        },
    }
}
</script>

<style scoped>
    .transferfooter {
        margin-left: 8px;
        padding: 6px 5px;
    }
</style>
