import request from '@/utils/request';
enum API {
  COMPANY_URL = '/company/',
}

export const company = () => request.get<any, any>(API.COMPANY_URL);
