import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QuizsService {
  userLoginStatus=false;
  constructor(private hc:HttpClient ) {}

  getData():Observable<any>{
    return this.hc.get<any>("http://localhost:3000/questions")
  }

  createUser(userObj):Observable<any>{
    return this.hc.post("/user/createuser",userObj)
  }

  loginUser(credentials):Observable<any>{
    return this.hc.post("/user/login",credentials)
  }
  
}
