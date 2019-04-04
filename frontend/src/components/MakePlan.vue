<template>
    <div>
        <div class="wrapper">
            <div class="title">生产调度</div>
            <div class="desc">
                <strong>加工排产</strong>
            </div>
        </div>
        <div class="row">
            <div class="title">播种</div>
        </div>
        <div class="row">
            <div class="title2">生产计划编号
                <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.key"
                    :label="item.key"
                    :value="item">
                </el-option>
            </el-select>
            </div>
        </div>
        <div class="row">
            <div class="title2">
                流水线
                <el-upload
                  class="upload-demo"
                  action="http://0.0.0.0:5000/upload1"
                  :on-change="handleChange"
                  :on-success="changeList1"
                  :file-list="fileList3"
                  :show-file-list="false"
                >
                      <el-button size="small" type="primary">点击上传</el-button>
                </el-upload>
                <span v-if="liushuixian">上传成功！</span>
            </div>
        </div>
        <div class="row">
            <div class="title2">
                产量
                <el-upload
                  class="upload-demo"
                  action="http://0.0.0.0:5000/upload1"
                  :on-change="handleChange"
                  :on-success="changeList2"
                  :file-list="fileList3"
                  :show-file-list="false"
                >
                      <el-button size="small" type="primary">点击上传</el-button>
                </el-upload>
                <span v-if="chanliang">上传成功！</span>
            </div>
        </div>
        <div class="row">
                <el-input
                    type="textarea"
                    :rows="2"
                    placeholder="备注"
                    v-model="textarea">
                </el-input>

            </div>
            <el-button size="small" type="primary" @click="dialogVisible=true">提交</el-button>
        <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width="70%"
            :before-close="handleClose">
            <div class="abc">
                <div>产量</div>
                <div>黑玉米：{{value['heiyumi']}}</div>
                <div>花玉米：{{value['huayumi']}}</div>
                <div>甜玉米：{{value['tianyumi']}}</div>
            </div>
            <div class="abc">
                <div>加工调度结果</div>
                 <el-table
                :data="makeinfo">
                <el-table-column
                    prop="index"
                    label="编号"
                ></el-table-column>
                <el-table-column
                    prop="sales"
                    label="时间"
                ></el-table-column>
               <el-table-column
                    prop="type"
                    label="工艺"
                ></el-table-column>
            </el-table>
            </div>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="dialogVisible = false">取 消</el-button>
                  <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            dialogVisible: false,
            textarea: '',
            value: '',
            options: '',
            fileList3: [],
            showTable: false,
            liushuixian: false,
            chanliang: false,
            info: [
                {index: 1,area: 844, sales:46781.58868},
                {index:2,area:216,sales:14416.7369},
                {index:3,area: 211,sales:5062.992336},
                {index:4,area: 634,sales:51948.64439},
                {index:5,area: 191,sales:18970.50743},
                {index:6,area: 46,sales:1970.391008},
                {index:7,area: 731,sales:49810.14297},
                {index:8,area: 93,sales:4662.084881},
                {index:9,area: 22,sales:1279.041389},
                {index:10,area: 852,sales:10647.50311},
                {index:11,area: 195,sales:2250.077921},
                {index:12,area: 647,sales:22843.04302},
                {index:13,area: 909,sales:24623.57528},
                {index:14,area: 151,sales:8389.203867},
                {index:15,area: 159,sales:6426.095151},
                {index:16,area: 174,sales:5343.279943},
                {index:17,area: 15,sales:1267.169354},
                {index:18,area: 93,sales:4850.361639},
                {index:19,area: 63,sales:5098.397943},
                {index:20,area: 436,sales:11294.19564},
                {index:21,area: 131,sales:154.8790608},
                {index:22,area: 227,sales:554.8727087},
                {index:23,area: 29,sales:1609.523743},
                {index:24,area: 813,sales:39161.67319},                    {index:25,area: 68,sales:3730.95616},
                {index:26,area: 441,sales:22280.91682},
                {index:27,area: 427,sales:4905.397987},
                {index:28,area: 972,sales:58944.06309},
                {index:29,area:555,sales:32362.55379},
                {index:30,area: 225,sales:15711.23059},
                {index:31,area: 467,sales:25655.85433},
                {index:32,area: 30,sales:2443.007314},
            ],
            makeinfo: [
                {index:1,area: 844, sales:'8:00-9:15', type:'清洗'},
                {index:2,area:216,sales:'10:15-11:10', type: '漂荡'},
                {index:3,area: 211,sales:"11:30-12:30", type: '冷却'},
                {index:4,area: 191,sales:"13:00-14:30", type: '摊晾'},
                {index:5,area: 46,sales:"14:50-16:30", type: '包装'},
                {index:6,area: 46,sales:"16:40-18:10", type: '杀菌'},
            ]
        }
    },
    mounted() {
        this.getPlan()
    },
    methods: {
        handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
        },
        handleChange(file, fileList) {},
        changeList1() {
            console.log('changeList')
            this.liushuixian = true
        },
        changeList2() {
            this.chanliang = true
        },
        getPlan() {
            axios.get('http://0.0.0.0:5000/getplan').then(res => {
                console.log(res.data.res)
                this.options = res.data.res
            })
        }
    }
}
</script>

<style lang="less" scoped>
.wrapper {
    margin-top: 100px;
    margin-left: 10px;
    text-align: left;
    .title {
        font-size: 40px;
    }
    .desc {
        margin-top: 20px;
    }
}
.el-textarea {
    width: 70%;
}
.row {
    text-align: left;
    .title {
        background: #eeeeee;
        padding: 10px;
    }
}
.abc {
    text-align: left;
}
</style>
