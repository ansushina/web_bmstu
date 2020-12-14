import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Comment} from '../../../models/dto/comment-dto.model';
import {ActivatedRoute, Router} from '@angular/router';
import {FilmService} from '../../../services/film.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})
export class CommentComponent implements OnInit {

  @Input() public comment: Comment;
  public edit = false;
  public lastValue;

  @Output() public deleteComment: EventEmitter<string> = new EventEmitter<string>();

  constructor(private route: ActivatedRoute, private router: Router, private filmService: FilmService) {
  }

  onDelete(): void {
    if (this.comment) {
      this.deleteComment.emit(this.comment.id.toString());
    }
  }

  getUsername(): string {
    return localStorage.getItem('username');
  }

  onSave(): void {
    this.filmService.updateComment(this.comment.film, this.comment.id, {text: this.comment.text}).subscribe(
      comment => {
        this.comment = comment;
        this.edit = false;
      }, error => console.log(error)
    );
  }

  onBack(): void {
    this.comment.text = this.lastValue;
    this.edit = false;
  }

  onEdit(): void {
    this.lastValue = this.comment.text;
    this.edit = true;
  }

  ngOnInit(): void {
  }

}
