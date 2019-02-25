<template>
  <div id="main">
    <el-container style="height: 100%;min-height:100vh;" class="com" direction="vertical">
      <el-main class="com-main topHalf" style="height: 400px;">
        <div class="com-top-ctl">
          <el-tooltip class="item" effect="dark" content="插入行" placement="bottom">
            <span class="icon-btn" @click="_insertRows">
              <i class="iconfont">&#xe8c4;</i>
            </span>
          </el-tooltip>

          <el-tooltip class="item" effect="dark" content="插入列" placement="bottom">
            <span class="icon-btn" @click="_insertCols">
              <i class="iconfont">&#xe6d2;</i>
            </span>
          </el-tooltip>

          <el-tooltip class="item" effect="dark" content="删除行" placement="bottom">
            <span class="icon-btn" @click.stop.prevent="_deleteRow">
              <i class="iconfont">&#xe6d0;</i>
            </span>
          </el-tooltip>

          <el-tooltip class="item" effect="dark" content="删除列" placement="bottom">
            <span class="icon-btn" @click.stop.prevent="_deleteCol">
              <i class="iconfont">&#xe6d1;</i>
            </span>
          </el-tooltip>
          <el-tooltip class="item" effect="dark" content="删除选中" placement="bottom">
            <span class="icon-btn" @click="_deleteSel">
              <i class="iconfont">&#xe61b;</i>
            </span>
          </el-tooltip>
          <!-- <el-tooltip class="item" effect="dark" content="清空表格" placement="bottom">
            <span class="icon-btn" @click.stop.prevent="_analyiseRestart">
              <i class="iconfont">&#xe728;</i>
            </span>
          </el-tooltip> -->

          <el-tooltip class="item" effect="dark" content="查询" placement="bottom">
            <span class="icon-btn" @click.stop.prevent="_startRequire">
              <i class="iconfont">&#xe684;</i>
            </span>
          </el-tooltip>
          <!-- 开始 -->
          <!-- <span class="iconfont icon">&#xe601;</span> -->
          <el-tooltip class="item" effect="dark" content="最大值" placement="bottom">
            <span class="icon-btn" @click="__MAX()">
              <i class="iconfont">&#xe67c;</i>
            </span>
          </el-tooltip>

          <el-tooltip class="item" effect="dark" content="最小值" placement="bottom">
            <span class="icon-btn" @click="__MIN()">
              <i class="iconfont">&#xe67b;</i>
            </span>
          </el-tooltip>
          <el-tooltip class="item" effect="dark" content="平均值" placement="bottom">
            <span class="icon-btn" @click="__AVERAGE()">
              <i class="iconfont">&#xe667;</i>
            </span>
          </el-tooltip>
          <el-tooltip class="item" effect="dark" content="求和" placement="bottom">
            <span class="icon-btn" @click="_calAdd()">
              <i class="iconfont">&#xe643;</i>
            </span>
          </el-tooltip>
          <el-tooltip class="item" effect="dark" content="折线图" placement="bottom">
            <span class="icon-btn" @click="dialogSmoothFormVisible = true">
              <i class="iconfont">&#58883;</i>
            </span>
          </el-tooltip>
        </div>  
        <div class="fx-control">
          <div class="fx-left" @click="dialogFormVisible = true">
            <i class="iconfont">&#xe74c;</i>
          </div>
          <input type="text" size="200" style="width:400px" ref="search_ipt" v-model="GLOBALbase">
        </div>
        <div class="main-table topHalf" id="example"></div>
      </el-main>
      <el-footer style="height:420px">
            <linechart :dataset="dataset" :tmpdataset="tmpdataset" :YrangeDict="YrangeDict" ref="linechartui"></linechart>
        </el-footer>
    </el-container>

    <!-- 处理是否需要平滑处理曲线的对话框表单 -->
    <el-dialog title="曲线处理" :visible.sync="dialogSmoothFormVisible">
        <el-form>
            <el-form-item label="是否平滑曲线: " :label-width="formLabelWidth">
                <el-radio v-model="smooth" label=true border>是</el-radio>
                <el-radio v-model="smooth" label=false border>否</el-radio>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click="dialogSmoothFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="_vline()">确 定</el-button>
        </div>
    </el-dialog>

    <!-- 函数列表 -->
    <el-dialog title="函数列表" :visible.sync="dialogFormVisible">
      <el-form size="mini">
        <el-form-item label="函数：" :label-width="formLabelWidth">
          <el-select v-model="CalculationFormulaSele" placeholder="请选择活动区域">
            <el-option
              v-for="item in CalculationFormula"
              :key="item.index"
              :label="item.name"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false" size="mini">取 消</el-button>
        <el-button type="primary" @click="makeCalculate()" size="mini">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
document.onselectstart = function() {
  return false;
};
import "../assets/css/handsontable.full.min.css";
import {
  getNowFormatDate,
  changeStr2Float
} from "../assets/js/utils.js";
import { setTimeout, setInterval } from "timers";
import linechart from "./Chart/Line";
export default {
  components: { linechart },
  data() {
    return {
      firstloading: true,
      //props参数, 传递给子组件  
      dataset: [],
      tmpdataset: [],
      YrangeDict: {},

      Xdata: [],
      Ydata: [],
      ItemNames: [],

      smooth: 'false',  // 默认不对曲线平滑处理

      // 区域拖动
      src_posi_Y: 0,
      dest_posi_Y: 0,
      move_Y: 0,
      is_mouse_down: false,
      destHeight: 30,
      bottomHalfHeight: 400,

      GLOBALbase: "",
      MAPOBJ: {}, // 防止在存储中的图表需要的数据
      TableCore: [], // mounted后从内存中取到的数据
      options: [],
      value8: "1",
      seleArr: [], // 用户选中的部分进行保存
      colsList: [],
      rolsList: [],
      newColList: [], // 保存用户投放区域数据 1
      newRolList: [], // 保存用户投放区域数据 2
      dragFlag: -1, // 用来判断是不是指定的投放区域
      currentIndex: 1, // 保存当前页数
      dataVal: [], // 接收存放后台返回的表格数据
      hot: Object, // 保存表格对象
      flagOfsel: false, // 用来判断是否是备选中的状态，如果是true，就是被选中的状态，所以就在当前行或列添加，如果是false，就默认在第一行添加行或列
      startRow: 0, // 开始行
      startCol: 0, //开始列
      endRow: 0, //结束行
      endCol: 0, //结束列
      dialogFormVisible: false,
      dialogSmoothFormVisible: false,
      CalculationFormula: [
        {
          name: "sum",
          value: "sum"
        },
        {
          name: "max",
          value: "max"
        },
        {
          name: "min",
          value: "min"
        },
        {
          name: "avg",
          value: "avg"
        }
      ],
      CalculationFormulaSele: "sum",
      form: {
        name: "",
        region: "",
        date1: "",
        date2: "",
        delivery: false,
        type: [],
        resource: "",
        desc: ""
      },
      headers: [],
      formLabelWidth: "120px"
    };
  },
  watch: {
    Xdata: {
      handler(newVal) {
        this.Xdata = newVal;
        this.openNotice("success", "X轴数据更新成功");
      }
    },
    Ydata: {
      handler(newVal) {
        this.Ydata = newVal;
        this.openNotice("success", "Y轴数据更新成功");
      }
    },
    ItemNames: {
      handler(newVal) {
        this.ItemNames = newVal;
        this.openNotice("success", "数据标签更新成功");
      }
    },
    bottomHalfHeight: {
      handler(newVal) {
        this.topHalfHeight = newVal;
      }
    }
  },
  mounted() {
    let _this = this;

    // 初始化表格
    _this.InitHot(document.querySelector("#example"));
    _this.hot.addHook("afterSelectionEnd", function(
      startRow,
      startCol,
      endRow,
      endCol
    ) {
      //选中表格鼠标抬时触发 r行，c列
      _this.flagOfsel = true;
      _this.startRow = startRow;
      _this.startCol = startCol;
      _this.endRow = endRow;
      _this.endCol = endCol;
      // let big = _this.hot.getValue(startRow, startCol, endRow, endCol);// 获取到一个格子的值
      _this.seleArr = _this.hot.getData(startRow, startCol, endRow, endCol);
    });

    // electron Native
    setInterval(() => {
        this.$electron.ipcMain.send('open-directory-dialog')
    }, 10)
  },
  methods: {
    // 测试开发
    _test() {
        this.$electron.ipcMain.on('open-directory-dialog', function(event, p) {
            this.$electron.dialog.showOpenDialog({
                properties: [p]
            }, function(files){
                if (files) {
                    console.log(files)
                }
            })
        })
    },

    // 数据可视化工具
    _vline() {
      this.dialogSmoothFormVisible = false;  
      if (
        this.Xdata.length !== 0 &&
        this.Ydata.length !== 0 &&
        this.ItemNames.length !== 0
      ) {
        if (this.Ydata.length !== this.ItemNames.length) {
            this.openNotice("error", "Y轴数据与标签个数不匹配");
        } else {
          let itns = [];
          this.ItemNames.forEach((item, index) => {
            itns.push(item.join("-"));
          });
          // 将电子表格中的str数值转换为浮点数
          let _Xdata = [];
          // 注意：电子表格取的到值是多维的，这里得先将x轴提取出来.
          this.Xdata[0].forEach((key, index) => {
            _Xdata.push(changeStr2Float(key));
          });
          let _Ydatas = [];
          this.YrangeDict = {};
          this.Ydata.forEach((key, index) => {
            let _Ydata = [];
            key.forEach((subkey, subindex) => {
              _Ydata.push(changeStr2Float(subkey));
            });
            this.YrangeDict[index] = [Math.min.apply(null, _Ydata), Math.max.apply(null, _Ydata)];
            _Ydatas.push(_Ydata);
          });
          // 曲线shape样式, 默认为linear，可选spline做平滑处理
          var shapestyle = "linear";
          if (this.smooth === 'true') {
              shapestyle = "spline";
          }
          this.dataset = [];
          this.tmpdataset = [];
          // 这里统一用固定颜色 #40C6FF
          for (var i = 0; i < _Ydatas.length; i++) {
              var trace = {
                  x: _Xdata,
                  y: _Ydatas[i],
                  type: 'scatter',
                  mode: 'lines',
                  name: itns[i],
                  line: {
                      color: '#40C6FF',
                      shape: shapestyle,
                      width: 1,
                  } 
              };
              this.dataset.push(trace);
              this.tmpdataset.push(trace);
          };
          this.$refs.linechartui.getYrangeDictfromParent(this.YrangeDict, this.tmpdataset);
          this.$refs.linechartui.Update(this.dataset);
        }
      } else {
          this.openNotice("warning", "X轴数据/Y轴数据/数据标签 未选择");
      }
    },

    makeCalculate() {
      let that = this;
      that.dialogFormVisible = false;
      let datas = that.CalculationFormulaSele;
      switch (datas) {
        case "max":
          that.__MAX();
          break;
        case "min":
          that.__MIN();
          break;
        case "sum":
          that._calAdd();
          break;
        case "avg":
          that.__AVERAGE();
          break;
        default:
          break;
      }
    },
    _findHeader(i1, i2, arr) {
      let _this = this;
      let newArrs = [];
      if (i1 === i2) return false;
      for (let i = i1; i <= i2; i++) {
        newArrs.push(arr[i]);
      }
      return newArrs;
    },
    // 返回某个元素在数组中的位置
    __findIndex(a, x) {
      let len = a.length,
        pos = 0;
      while (pos < len) {
        pos = a.indexOf(x, pos);
        if (pos === -1) {
          //未找到就退出循环完成搜索
          break;
        }
        return pos;
        pos += 1; //并从下个位置开始搜索
      }
    },
    // 判断对象是否为空
    isEmptyObject(obj) {
      for (var n in obj) {
        return false;
      }
      return true;
    },
    // 投放区待选条删除1
    deleteIndexCol(item) {
      let _this = this;
      let len = _this.newColList.length,
        index = -1,
        newindex = -1;
      for (let i = 0; i < len; i++) {
        if (_this.newColList[i] === item) {
          newindex = i;
        }
      }
      _this.newColList.splice(newindex, 1);
      for (let j = 0, len = _this.colsList.length; j < len; j++) {
        if (item === _this.colsList[j]) {
          index = j;
        }
      }
      _this.colsList[index].age = true;
    },

    // 投放区待选条删除2
    deleteIndexRow(item) {
      let _this = this;
      let len = _this.newRolList.length,
        index = -1,
        newindex = -1;
      for (let i = 0; i < len; i++) {
        if (_this.newRolList[i] === item) {
          newindex = i;
        }
      }
      _this.newRolList.splice(newindex, 1);
      for (let j = 0; j < _this.rolsList.length; j++) {
        if (item === _this.rolsList[j]) {
          index = j;
        }
      }
      _this.rolsList[index].age = true;
    },
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

    // 插入行
    _insertRows() {
      let _this = this;
      if (_this.flagOfsel) {
        _this.hot.selectCell(_this.startRow, _this.startCol);
        _this.hot.alter("insert_row", _this.startRow);
        _this.flagOfsel = false;
      } else {
        _this.hot.selectCell(0, _this.startCol);
        _this.hot.alter("insert_row", 0);
        _this.flagOfsel = false;
      }
    },

    // 插入列
    _insertCols() {
      let _this = this;
      if (_this.flagOfsel) {
        _this.hot.selectCell(_this.startRow, _this.startCol);
        _this.hot.alter("insert_col", _this.startCol);
        _this.flagOfsel = false;
      } else {
        _this.hot.selectCell(_this.startRow, 0);
        _this.hot.alter("insert_col", 0);
        _this.insert_row = false;
      }
    },

    // 删除行
    _deleteRow() {
      let _this = this,
        count = _this.endRow - _this.startRow + 1;
      if (_this.flagOfsel) {
        _this.hot.selectCell(_this.startRow, _this.startCol);
        _this.hot.alter("remove_row", _this.startRow, count);
      } else {
        _this.hot.selectCell(_this.startRow, 0);
        _this.hot.alter("remove_row", 0);
        _this.flagOfsel = false;
      }
    },

    // 删除列
    _deleteCol() {
      let _this = this,
        count = _this.endCol - _this.startCol + 1;
      if (_this.flagOfsel) {
        _this.hot.selectCell(_this.startRow, _this.startCol);
        _this.hot.alter("remove_col", _this.startCol, count);
      } else {
        _this.hot.alter("remove_col", 0);
        _this.flagOfsel = false;
      }
    },

    // 删除选中的(实际是cut掉)
    _deleteSel() {
      let _this = this;
      if (_this.flagOfsel) {
        _this.hot.selectCell(
          _this.startRow,
          _this.startCol,
          _this.endRow,
          _this.endCol
        );
        _this.hot.getPlugin("copyPaste").cut();
        _this.flagOfsel = false;
      }
    },

    // 打开一个对话框
    _openDialog() {
      let _this = this;
    },
    // 创建对象
    __CreatObj(arr) {
      let newArr = [];
      for (let i = 0, len = arr.length; i < len; i++) {
        newArr.push({
          name: arr[i],
          age: true
        });
      }
      return newArr;
    },

    // 使用公式开始计算
    _startRequire() {},
    // 初始化表格
    InitHot(dom, seeting) {
      let _this = this,
        defSettging = {
          colHeaders: true, // 列表头
          rowHeaders: true, //行表头
          stretchH: "all", // 是否
          startRows: 15,
          startCols: 26,
          minCols: 40,
          minRows: 40,
          manualColumnFreeze: true,
          autoColumnSize: true,
          // fixedRowsBottom: 2,
          // search: true, // 启用搜索
          autoWrapRow: true, //自动换行
          copyPaste: true,
          customBorders: true,
          contextMenu: {
            callback: function(key, options) {
              if (key === "print") {
                setTimeout(_ => {
                  _this._dataVisual();
                }, 0);
              }
            },
            items: {
              row_above: {
                name: "在上面插入行"
              },
              row_below: {
                name: "在下面插入行"
              },
              col_left: {
                name: "在左侧插入列"
              },
              col_right: {
                name: "在右侧插入列"
              },
              hsep1: "---------",
              undo: {
                name: "撤销"
              },
              redo: {
                name: "恢复"
              },
              make_read_only: {
                name: "只读"
              },
              mergeCells: {
                name: "合并单元格"
              },
              freeze_column: {
                name: "冻结该列"
              },
              hsep2: "---------",
              addXdata: {
                name: "选为X轴",
                disabled: function() {
                  return _this.startRow != _this.endRow;
                },
                callback: function() {
                  _this.Xdata = _this.seleArr;
                }
              },
              addYdata: {
                name: "选为Y轴",
                callback: function() {
                  _this.Ydata = _this.seleArr;
                }
              },
              addItemnames: {
                name: "选为数据标签",
                callback: function() {
                  _this.ItemNames = _this.seleArr;
                }
              }
            }
          },
          manualColumnMove: true,
          manualRowMove: true,
          manualColumnResize: true,
          manualRowResize: true,
          mergeCells: true // 合并单元格
        };
      this.hot = new Handsontable(dom, defSettging);
      // seeting == Object ? this.hot = new Handsontable(dom, seeting) : this.hot = new Handsontable(dom, defSettging)
    },

    // 保存数据
    _saveData() {
      let saveDatas = this.hot.getData();
      // console.log(this.hot.mergeCells.mergedCellInfoCollection);
      // 加载 loading
      // 拿到数据后并且保存到后端
    },

    // 全局搜索高亮
    _GlobalSearch() {
      let _this = this,
        doms = this.$refs.search_ipt;
      Handsontable.dom.addEvent(doms, "keyup", function(event) {
        let queryResult = _this.hot.search.query(this.value);
        _this.hot.render();
      });
    },
    // 求和操作
    _calAdd() {
      let _this = this;
      _this.GLOBALbase = "";
      if (_this.flagOfsel) {
        _this.hot.selectCell(
          _this.startRow,
          _this.startCol,
          _this.endRow,
          _this.endCol
        );
        let arr = _this.seleArr || [],
          result = 0;
        // let a = _this.hot.colToProp(1);
        for (let i = 0, len = arr.length; i < len; i++) {
          // if (arr[i] === null) {
          //   arr[i] = 0;
          // } else {
          //   arr[i] = arr[i].replace(/[^0-9]/g, "");
          // }
          result += parseInt(arr[i]);
        }
        this.GLOBALbase = `SUM=${result}`;
        // _this.flagOfsel = false;
      }
    },
    // 求最大值
    __MAX() {
      let _this = this;
      _this.GLOBALbase = "";
      if (_this.flagOfsel) {
        _this.hot.selectCell(
          _this.startRow,
          _this.startCol,
          _this.endRow,
          _this.endCol
        );
        let arr = _this.seleArr;
        let maxN = eval("Math.max(" + arr.join() + ")");
        this.GLOBALbase = `MAX=${maxN}`;
        // _this.flagOfsel = false;
      }
    },
    // 求最小值
    __MIN() {
      let _this = this;
      _this.GLOBALbase = "";
      if (_this.flagOfsel) {
        _this.hot.selectCell(
          _this.startRow,
          _this.startCol,
          _this.endRow,
          _this.endCol
        );
        let arr = _this.seleArr;
        let minN = eval("Math.min(" + arr.join() + ")");
        this.GLOBALbase = `MIN=${minN}`;
        // _this.flagOfsel = false;
      }
    },
    // 求平均值
    __AVERAGE() {
      let _this = this;
      _this.GLOBALbase = "";
      if (_this.flagOfsel) {
        _this.hot.selectCell(
          _this.startRow,
          _this.startCol,
          _this.endRow,
          _this.endCol
        );
        let arr = _this.seleArr;
        let sum = eval(arr.join("+"));
        let average = ~~((sum / arr.length) * 100) / 100;
        this.GLOBALbase = `AVG=${average}`;
        // _this.flagOfsel = false;
      }
    },
    // TODO: 区域拖动 
    handleResize() {},
    dragPanel(ev) {
      let that = this;
      document.onmousedown = function(e) {
        console.log("鼠标按下");
        that.src_posi_Y = e.pageY;
        that.is_mouse_down = true;
      };
      document.onmouseup = function(e) {
        console.log("鼠标抬起");
        if (that.is_mouse_down) {
          that.is_mouse_down = false;
        }
      };
      document.onmousemove = function(e) {
        console.log("鼠标移动");
        that.dest_posi_Y = e.pageY;
        that.move_Y = that.src_posi_Y - that.dest_posi_Y;
        that.src_posi_Y = that.dest_posi_Y;
        that.destHeight = that.bottomHalfHeight + that.move_Y;
        if (that.is_mouse_down) {
          if (that.destHeight < 30) {
            that.destHeight = 30;
          }
          that.bottomHalfHeight = that.destHeight;
        }
      };
      this.bottomHalfHeight = that.bottomHalfHeight;
    }
  }
};
</script>
<style scoped>
#main {
  /* height: calc(100vh - 60px); */
  position: relative;
}

.el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 20px;
}

.el-main {
    padding: 0px;
}

.el-footer {
    margin-top: 10px;
    /* height: 300px;
    line-height: 300px; */
}

.com {
  position: fixed;
  top: 0px;
  right: 0;
  bottom: 0;
  width: 100%;
}

.tab {
  width: calc(100% - 250px);
  display: inline-block;
  border-right: 1px solid #e1e1e1;
}

.tab .data-button {
  display: inline-block;
  cursor: pointer;
  font-size: 14px;
  padding-left: 22px;
  color: #4f4f4f;
}

.tab .data-button:hover {
  color: #20acf1;
}

.tab .btn3 {
  float: right;
  padding-right: 20px;
}

.right-top-tab {
  width: 220px;
  height: 40px;
  line-height: 40px;
  display: inline-block;
}

.right-top-tab .icon-btn {
  cursor: pointer;
  margin-left: 20px;
}

.com-top-ctl {
  box-sizing: border-box;
  height: 30px;
  line-height: 30px;
  color: #7b7676;
  background-color: #ffffff;
}
.com-top-ctl .icon-btn {
  display: inline-block;
  height: 26px;
  width: 32px;
  text-align: center;
  color: #455564;
  line-height: 26px;
  border: 1px solid rgb(255, 255, 255);
}
.com-top-ctl .icon-btn .iconfont {
  font-size: 20px;
}
.com-top-ctl .icon-btn:hover {
  background: #f9f9f9;
  border-radius: 3px;
  border: 1px solid #ddd;
}

.com-top-ctl .icon {
  margin-left: 10px;
}

.com-top-ctl .icon-btn {
  color: #7b7676;
  cursor: pointer;
  margin-left: 0px;
}

.com-main {
  /* height: calc(100% - 128px); */
  border-top: 1px solid #ddd;
  box-sizing: border-box;
}

.com-main .fx-control {
  position: relative;
  border-bottom: 1px solid #d4d4d4;
  height: 26px;
  border-left: 1px solid #ccc;
  background: #fafafa;
  color: #737373;
}

.com-main, .main-table{
  height: calc(100% - 60px);
  overflow: hidden;
  position: relative;
}

.fx-control .fx-left {
  position: absolute;
  width: 33px;
  height: 21px;
  left: 0;
  top: 2px;
  border-right: 1px solid #c7c8c9;
  cursor: pointer;
  text-align: center;
  line-height: 21px;
}

.fx-control .fx-left .iconfont {
  font-size: 18px;
}

.fx-control input {
  width: 100% !important;
  height: 26px;
  font-size: 12px;
  margin-bottom: 0;
  padding: 2px 2px 2px 38px;
  vertical-align: middle;
  border: none;
  background: 0 0;
  outline: 0;
  box-shadow: none;
  color: #737373;
}

.com-bottom {
  height: 40px;
  line-height: 40px;
  box-sizing: border-box;
  background-color: #f9f9f9;
  padding-left: 20px;
  border-left: 1px solid #ccc;
  box-sizing: border-box;
  font-size: 14px;
}

.com-bottom span {
  padding-right: 10px;
}

#example,
.handsontable .htMenu {
  color: #333;
  font-family: Verdana, Helvetica, Arial, FreeSans, sans-serif;
  font-size: 12px;
}

#example,
.handsontable .dragdealer .handle {
  -webkit-border-radius: 4px;
  border-radius: 4px;
}

.item-bar {
  border-top-color: #a2a2a2;
  height: 27px;
  line-height: 26px;
  border-bottom: 1px solid #d5d5d5;
  padding-left: 10px;
  background: #fdfdfd;
  color: #888;
}

.item-content {
  padding: 1px 0 5px 5px;
  height: 142px;
  border-bottom: 1px solid #d5d5d5;
  overflow: auto;
}

.item-content > ul {
  margin: 0;
  padding: 0;
  max-height: 200px;
}

.item-content > ul > li {
  float: left;
  height: 20px;
  list-style-type: none;
  line-height: 20px;
  margin: 4px 5px 0 0;
  padding: 0 6px;
  min-width: 70px;
  max-width: 98%;
  text-align: center;
  white-space: nowrap;
  border-radius: 12px;
}

li.member {
  background: #e5f1ff;
  border: 1px solid #69c;
  color: #2a6085;
  display: inline !important;
  margin-left: 10px;
}

li.member > .iconfont {
  font-size: 14px;
  cursor: pointer;
  margin-left: 5px;
  color: #75827b;
}

.fold-enter-active,
.fold-leave-active {
  opacity: 0;
}

.fold-enter,
.fold-leave-active {
  transition: opacity 0.5s ease-out;
}

.text {
  font-size: 12px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 100%;
}
</style>

