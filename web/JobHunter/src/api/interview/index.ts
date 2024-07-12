//统一管理咱们项目用户相关的接口

import request from '@/utils/request';

// import type { loginFormData, loginResponseData, userInfoReponseData } from './type';

//项目用户相关的请求地址

enum API {
  INTERVIEW_URL = '/',
  COMPANY_URL = '/company/',
  JOB_URL = '/job/',
}

export const interview = () => request.get<any, any>(API.INTERVIEW_URL);
export const company = () => request.get<any, any>(API.COMPANY_URL);
export const job = () => request.get<any, any>(API.JOB_URL);
export const getInterviewById = (id: any) => request.get<any, any>(API.INTERVIEW_URL + id + '/');
export const createInterview = (data:any) => request.post<any, any>(API.INTERVIEW_URL, data);