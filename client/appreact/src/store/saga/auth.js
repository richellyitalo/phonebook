import { call, put } from 'redux-saga/effects';
import api from '../../services/api';

import AuthActions from '../ducks/auth';

export function* signIn({ username, password }) {
  try {
    const response = yield call(api.post, 'login', { username, password });

    localStorage.setItem('@token', response.data.token);

    yield put(AuthActions.signInSuccess(response.data.token));
  } catch (err) {
    console.log(err);
  }
}
