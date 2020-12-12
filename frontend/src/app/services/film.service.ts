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
                    genres: [],
                    actors: [],
                    countries: [],
                    yearFrom: 0,
                    yearTo: 0
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
      str += `query=${params.query}&`;
    }

    if (params.genres) {
      params.genres.map((g, i) => {
        str += `genre=${g}&`;
      });
    }

    if (params.actors) {
      params.actors.map((g, i) => {
        str += `actor=${g}&`;
      });
    }

    if (params.countries) {
      params.countries.map((g, i) => {
        str += `country=${g}&`;
      });
    }

    if (params.yearFrom) {
      str += `year_from=${params.yearFrom}&`;
    }

    if (params.yearTo) {
      str += `year_to=${params.yearTo}&`;
    }

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

  public getComments(id: number): Observable<Comment[]> {
    return this.http.get<Comment[]>(`${this.url}/${id}/comments/`);
  }

  public getComment(filmId: number, id: number): Observable<Comment> {
    return this.http.get<Comment>(`${this.url}/${filmId}/comments/${id}/`);
  }

  public createComment(id: number, source: Comment): Observable<Comment> {
    return this.http.post<Comment>(`${this.url}/${id}/comments/`, source);
  }

  public updateComment(filmId: number, id: number, source: Comment): Observable<Comment> {
    return this.http.patch<Comment>(`${this.url}/${filmId}/comments/${id}/`, source);
  }

  public deleteComment(filmId: number, id: number): Observable<any> {
    return this.http.delete(`${this.url}/${filmId}/comments/${id}/`);
  }

  public createLike(filmId: number, source: Like): Observable<Like> {
    return this.http.post<Like>(`${this.url}/${filmId}/likes/`, source);
  }

  public getLike(filmId: number, userId: number): Observable<Like> {
    return this.http.get<Like>(`${this.url}/${filmId}/likes/${userId}/`);
  }

  public updateLike(filmId: number, userId: number, source: Like): Observable<Like> {
    return this.http.patch<Like>(`${this.url}/${filmId}/likes/${userId}/`, source);
  }
}
