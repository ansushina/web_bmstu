import {Component, EventEmitter, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-comment-input',
  templateUrl: './comment-input.component.html',
  styleUrls: ['./comment-input.component.scss']
})
export class CommentInputComponent implements OnInit {

  constructor() { }

  @Output() public addComment: EventEmitter<string> = new EventEmitter<string>();
  public comment = '';

  onAddComment(): void {
    if (this.comment) {
      this.addComment.emit(this.comment);
      this.comment = '';
    }
  }

  ngOnInit(): void {
  }

}
