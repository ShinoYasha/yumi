<template>
  <div id="app">
    <el-row class="tac">
      <el-col>
        <h5>生产计划管理平台</h5>
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>销售数据</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1" @click="upload">导入销售数据</el-menu-item>
              <el-menu-item index="1-2" @click="manage">数据管理</el-menu-item>
              <el-menu-item index="1-3" @click="predict">销量预测</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>生产计划</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="2-1">新计划</el-menu-item>
              <el-menu-item index="2-2">生产中</el-menu-item>
              <el-menu-item index="2-3">已完成</el-menu-item>
              <el-menu-item index="2-3">管理</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-col>
    </el-row>

    <div class="right">
      <upload-csv v-if="showUploadCsv"></upload-csv>
      <data-manage v-if="showDataManage"></data-manage>
      <sale-predict v-if="showSalePredict"></sale-predict>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import UploadCsv from "./components/UploadCsv.vue";
import DataManage from './components/DataManage.vue'
import SalePredict from './components/SalePredict.vue'
export default {
  name: "App",
  components: { UploadCsv, DataManage, SalePredict },
  data() {
    return {
      showUploadCsv: false,
      showDataManage: false,
      showSalePredict: false,
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    upload() {
      this.showUploadCsv = true;
      this.showDataManage = false;
      this.showSalePredict = false
    },
    manage() {
        this.showUploadCsv = false;
        this.showDataManage = true
        this.showSalePredict = false
    },
    predict() {
        this.showUploadCsv = false;
        this.showDataManage = false
        this.showSalePredict = true
    }
  },
  mounted() {
    axios.get("http://0.0.0.0:5000/clear");
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
}
.tac {
  width: 20%;
}
.right {
  flex-grow: 1;
  padding: 10px;
}
</style>
