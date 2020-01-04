import { createReducer, createActions } from 'reduxsauce';
import Immutable from 'seamless-immutable';

// Types e actions
const { Types, Creators } = createActions({
  signInRequest: ['username', 'password'],
  signInSuccess: ['token']
});

export const AuthTypes = Types;
export default Creators;

// Estado inicial
export const INITIAL_STATE = Immutable({
  signedIn: false,
  token: null
});

// reducers
export const success = (state, { token }) => {
  console.log(token);
  state.merge({ signedIn: true, token });
};
// state.merge({ signedIn: true, token });

export const reducer = createReducer(INITIAL_STATE, {
  [Types.SIGN_IN_SUCCESS]: success
});
