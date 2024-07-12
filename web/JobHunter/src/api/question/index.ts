//统一管理咱们项目用户相关的接口

import request from '@/utils/request';

// import type { loginFormData, loginResponseData, userInfoReponseData } from './type';

//项目用户相关的请求地址

enum API {
  QUESTION_URL = 'question/',

  SUBJECT_URL = '/subject/',

  COMPANY_URL = '/company/',

  JOB_URL = '/job/',
}

export const question = (params: any) => request.get<any, any>(API.QUESTION_URL, { params });
export const getQuestionById = (id: any) => request.get<any, any>(API.QUESTION_URL + id + '/');
export const createQuestion = (data: any) => request.post<any, any>(API.QUESTION_URL, data);
export const subject = () => request.get<any, any>(API.SUBJECT_URL);
export const company = () => request.get<any, any>(API.COMPANY_URL);
export const job = () => request.get<any, any>(API.JOB_URL);
