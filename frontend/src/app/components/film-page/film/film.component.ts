import {Component, Input, OnInit} from '@angular/core';
import {Film} from '../../../models/dto/film-dto.model';
import {Like} from '../../../models/dto/like-dto.model';
import {FilmService} from '../../../services/film.service';

@Component({
  selector: 'app-film',
  templateUrl: './film.component.html',
  styleUrls: ['./film.component.scss']
})
export class FilmComponent implements OnInit {

  @Input() public film: Film;

  constructor(private filmService: FilmService) {
  }

  @Input() public lastLike: Like;


  @Input() public like: Like;

  likes = [{value: 10, text: 'не оценено'},
    {value: 1, text: '1'},
    {value: 2, text: '2'},
    {value: 3, text: '3'},
    {value: 4, text: '4'},
    {value: 5, text: '5'}];


  onLikeChange(): void {
    console.log('change', this.like.id, this.like.value);
    if (!this.like.id) {
      this.filmService.createLike(this.film.id, {value: this.like.value}).subscribe(
        like => {
          this.like = like;
        },
        error => console.log(error)
      );
    } else if (this.like.value === '10') {
      this.filmService.deleteLike(this.film.id, localStorage.getItem('username')).subscribe(
        res => this.lastLike = this.like,
        error => console.log(error)
      );
    } else {
      this.filmService.updateLike(this.film.id, localStorage.getItem('username'), {value: this.like.value})
        .subscribe(
          like => {
            this.like = like;
          },
          error => console.log(error)
        );
    }
  }


  ngOnInit(): void {
  }

  isAuth(): boolean {
    return localStorage.getItem('username') !== null;
  }

}
