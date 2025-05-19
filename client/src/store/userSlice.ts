import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

interface UserState {
  username: string | null;
  token: string | null;
}

const initialState: UserState = {
  username: null,
  token: null,
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    login(state, action: PayloadAction<{ username: string; token: string }>) {
      state.username = action.payload.username;
      state.token = action.payload.token;
    },
    logout(state) {
      state.username = null;
      state.token = null;
    },
  },
});

export const { login, logout } = userSlice.actions;
export default userSlice.reducer;
