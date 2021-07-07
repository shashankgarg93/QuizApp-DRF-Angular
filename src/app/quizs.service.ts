import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QuizsService {

  constructor(private hc:HttpClient ) {}

  getData():Observable<any>{
    return this.hc.get<any>("http://localhost:3000/questions")
  }
  
}
