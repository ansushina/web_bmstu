import {Injectable} from '@angular/core';

import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';
import {Film} from '../models/dto/film-dto.model';
import {Like} from '../models/dto/like-dto.model';
import {Comment} from '../models/dto/comment-dto.model';

@Injectable()
export class FilmService {

  private url = `${environment.baseUrl}/api/v1/films`;

  constructor(private http: HttpClient) {
  }


  public getFilms(sort = '',
                  offset = -1,
                  limit = -1,
                  params = {
                    query: '',
                    genre: [],
                    actor: [],
                    country: [],
                    yearFrom: -1,
                    yearTo: -1
                  }): Observable<Film[]> {
    let str = '?';
    if (sort !== '') {
      str += 'sort=' + sort + '&';
    }
    if (offset >= 0) {
      str += `offset=${offset}&`;
    }
    if (limit > 0) {
      str += `limit=${limit}&`;
    }

    if (params.query) {
      str += `q=${params.query}&`;
    }

    if (params.genre) {
      params.genre.map((g, i) => {
        str += `genre=${g}&`;
      });
    }

    if (params.actor) {
      params.actor.map((g, i) => {
        str += `actor=${g}&`;
      });
    }

    if (params.country) {
      params.country.map((g, i) => {
        str += `country=${g}&`;
      });
    }

    if (params.yearFrom > 0) {
      str += `year_from=${params.yearFrom}&`;
    }

    if (params.yearTo > 0) {
      str += `year_to=${params.yearTo}&`;
    }

    console.log(str);

    return this.http.get<Film[]>(`${this.url}/${str}`);
  }

  public getFilm(id: number): Observable<Film> {
    // let myHeaders;
    // if (localStorage.getItem('user-token')) {
    //   myHeaders = new HttpHeaders({
    //     Authorization: 'Bearer ' + localStorage.getItem('user-token'),
    //   });
    // }
    return this.http.get<Film>(`${this.url}/${id}/`);
  }

  public getComments(id: number,
                     offset = -1,
                     limit = -1): Observable<Comment[]> {
    let str = '?';
    if (offset >= 0) {
      str += `offset=${offset}&`;
    }
    if (limit > 0) {
      str += `limit=${limit}&`;
    }
    return this.http.get<Comment[]>(`${this.url}/${id}/comments/${str}`);
  }

  public getComment(filmId: number, id: number): Observable<Comment> {
    return this.http.get<Comment>(`${this.url}/${filmId}/comments/${id}/`);
  }

  public createComment(id: number, source: Comment): Observable<Comment> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.post<Comment>(`${this.url}/${id}/comments/`, source, {headers: myHeaders});
  }

  public updateComment(filmId: number, id: number, source: Comment): Observable<Comment> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.patch<Comment>(`${this.url}/${filmId}/comments/${id}/`, source, {headers: myHeaders});
  }

  public deleteComment(filmId: number, id: number): Observable<any> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.delete(`${this.url}/${filmId}/comments/${id}/`, {headers: myHeaders});
  }

  public createLike(filmId: number, source: Like): Observable<Like> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.post<Like>(`${this.url}/${filmId}/likes/`, source, {headers: myHeaders});
  }

  public getLike(filmId: number, username: string): Observable<Like> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.get<Like>(`${this.url}/${filmId}/likes/${username}/`, {headers: myHeaders});
  }

  public updateLike(filmId: number, username: string, source: Like): Observable<Like> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.patch<Like>(`${this.url}/${filmId}/likes/${username}/`, source, {headers: myHeaders});
  }

  public deleteLike(filmId: number, username: string): Observable<any> {
    let myHeaders;
    if (localStorage.getItem('user-token')) {
      myHeaders = new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('user-token'),
      });
    }
    return this.http.delete(`${this.url}/${filmId}/likes/${username}/`, {headers: myHeaders});
  }
}
