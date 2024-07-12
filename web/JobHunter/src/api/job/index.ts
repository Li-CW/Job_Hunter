import request from '@/utils/request';
enum API {
  JOB_URL = '/job/',
}

export const job = () => request.get<any, any>(API.JOB_URL);
