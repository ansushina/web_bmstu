import {Component, OnInit} from '@angular/core';
import {Film} from '../../models/dto/film-dto.model';
import {Comment} from '../../models/dto/comment-dto.model';
import {ActivatedRoute} from '@angular/router';
import {FilmService} from '../../services/film.service';
import {Like} from '../../models/dto/like-dto.model';

@Component({
  selector: 'app-film-page',
  templateUrl: './film-page.component.html',
  styleUrls: ['./film-page.component.scss']
})
export class FilmPageComponent implements OnInit {

  public film: Film;
  public comments: Comment[];
  public like: Like;
  private id: number;
  public error;

  constructor(private route: ActivatedRoute, private filmService: FilmService) {
    this.id = +this.route.snapshot.paramMap.get('id');
  }

  isAuth(): boolean {
    return localStorage.getItem('username') !== null;
  }

  onAddComment(comment: string): void {
    this.filmService.createComment(this.id, {text: comment}).subscribe(
      newComment => this.comments.push(newComment),
      error => console.log(error)
    );
  }

  onDeleteComment(id: string): void {
    // tslint:disable-next-line:radix
    this.filmService.deleteComment(this.id, parseInt(id)).subscribe(
      res => {
        let index: number;
        this.comments.map((el, i) => {
          // tslint:disable-next-line:radix
          if (el.id === parseInt(id)) {
            index = i;
          }
        });
        this.comments.splice(index, 1);
      }
    );
  }

  ngOnInit(): void {
    this.filmService.getFilm(this.id).subscribe(
      film => this.film = film,
      err => this.error = err
    );

    this.filmService.getComments(this.id, 0, 100).subscribe(
      comments => this.comments = comments,
      error => this.error = error
    );

    if (localStorage.getItem('username')) {
      // tslint:disable-next-line:radix
      this.filmService.getLike(this.id, localStorage.getItem('username')).subscribe(
        like => this.like = like,
        error => {
          this.like = {value: '10'};
        },
      );
    }
  }
}
