import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';
import {Genre} from "../models/dto/genre-dto.model";
import {Actor} from "../models/dto/actor-dto.model";
import {Country} from "../models/dto/country-dto.model";
@Injectable({
  providedIn: 'root'
})
export class FiltersService {
  private url = `${environment.baseUrl}/api/v1`;

  constructor(private http: HttpClient) {
  }

  public getGenres(): Observable<Genre[]> {
    return this.http.get<Genre[]>(`${this.url}/genres/`);
  }

  public getActors(): Observable<Actor[]> {
    return this.http.get<Actor[]>(`${this.url}/actors/`);
  }

  public getCountries(): Observable<Country[]> {
    return this.http.get<Country[]>(`${this.url}/countries/`);
  }
}
