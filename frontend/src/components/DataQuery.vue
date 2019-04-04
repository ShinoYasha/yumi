<template>
    <div>
        <div class="wrapper">
            <div class="title">生产计划</div>
            <div class="desc">
                <strong>数据查询</strong>
            </div>
        </div>
        <div class="row">
            <div class="title">需求预测量</div>
            <el-date-picker
                v-model="value1"
                type="date"
                placeholder="选择日期">
            </el-date-picker>
            <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <el-button type="primary">确定</el-button>
        </div>
        <div class="row">
            <div class="title">线上零售下单总量</div>
            <el-date-picker
                v-model="value1"
                type="date"
                placeholder="选择日期">
            </el-date-picker>
            <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <el-button type="primary">确定</el-button>
        </div>
        <div class="row">
            <div class="title">现有库存量</div>
            <el-date-picker
                v-model="value1"
                type="date"
                placeholder="选择日期">
            </el-date-picker>   
            <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>     
            <el-button type="primary">确定</el-button>
        </div>
        <div class="row">
            <div class="title">安全库存量</div>
            <el-date-picker
                v-model="value1"
                type="date"
                placeholder="选择日期">
            </el-date-picker>
            <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>   
            <el-button type="primary">确定</el-button>
        </div>
        <div class="row">
            <div class="title">工艺路线</div>
            <el-date-picker
                v-model="value1"
                type="date"
                placeholder="选择日期">
            </el-date-picker>
            <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>   
            <el-button type="primary">确定</el-button>
        </div>
        <div class="row">
            <div class="title">查询结果</div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            value: '',   
            value1: '',
            options: [],
            tableData: [],
        }
    },
    mounted() {
        this.getList()
    },
    methods: {
        getList() {
            axios.get("http://0.0.0.0:5000/getlist").then(res => {
                this.tableData = res.data.res
                for(let i in this.tableData) {
                    console.log(i)
                    let o = {
                        value: i,
                        label: this.tableData[i].class
                    }
                    console.log(o)
                    this.options.push(o)
                }
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
.row {
    text-align: left;
    .title {
        padding: 10px;
        background: #eeeeee;
    }
}
</style>
