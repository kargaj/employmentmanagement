import { createRouter, createWebHistory } from 'vue-router'
import { ROUTES } from "../constants/routes";

const routes = [
  {
    path: "/",
    redirect: "/employers"
  },
  {
    path: "/employers",
    name: ROUTES.EMPLOYERS,
    component: () => import("../components/EmployersListView.vue"),
  }, {
    path: "/employers/add",
    name: ROUTES.EMPLOYER_ADD,
    component: () => import("../components/EmployerAddView.vue"), 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
