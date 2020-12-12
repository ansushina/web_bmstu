import {Injectable} from '@angular/core';

import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';
import {User} from '../models/dto/user-dto.model';
import {Session} from '../models/dto/session-dto.model';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private url = `${environment.baseUrl}/api/v1`;
  private token;

  constructor(private http: HttpClient) {
  }

  public createUser(source): Observable<User> {
    return this.http.post<User>(`${this.url}/users/`, source);
  }

  public getUser(username: string): Observable<User> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.get<User>(`${this.url}/users/${username}/`, {headers: myHeaders});
  }

  public updateUser(username: string, source): Observable<User> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.patch<User>(`${this.url}/users/${username}/`, source, {headers: myHeaders});
  }

  public login(username: string, password: string): Observable<Session> {
    const source = {
      username,
      password,
    };
    return this.http.post<Session>(`${this.url}/sessions/`, source);
  }

  public logout(): void {
    localStorage.removeItem('user-token');
    localStorage.removeItem('username');
    localStorage.removeItem('id');
  }

  public get logIn(): boolean {
    return (localStorage.getItem('user-token') !== null);
  }

  public getJwtToken(): string {
    return (localStorage.getItem('user-token'));
  }

  public removeToken(): void {
    (localStorage.removeItem('user-token'));
  }
}
