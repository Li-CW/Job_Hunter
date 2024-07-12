import request from '@/utils/request';
enum API {
  LOGIN_URL = '/user/token/',
  REGISTER_URL = '/user/register/',
  REFRESH_TOKEN_URL = '/user/token/refresh/',
  FAVORITE_QUESTION_URL = '/favorite/question/',
  FAVORITE_INTERVIEW_URL = '/favorite/interview/',
}

export const login = (data:any) => request.post<any, any>(API.LOGIN_URL, data);
export const register = (data:any) => request.post<any, any>(API.REGISTER_URL, data);
export const refreshToken = (data:any) =>request.post(API.REFRESH_TOKEN_URL, data)
export const favoriteQuestion = () =>request.get(API.FAVORITE_QUESTION_URL)
export const favoriteInterview = () =>request.get(API.FAVORITE_INTERVIEW_URL)
export const createFavoriteQuestion = (data:any) =>request.post(API.FAVORITE_QUESTION_URL, data)
export const createFavoriteInterview = (data:any) =>request.post(API.FAVORITE_INTERVIEW_URL, data)