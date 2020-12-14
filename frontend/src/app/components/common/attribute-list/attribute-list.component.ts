import {Component, Input, OnInit} from '@angular/core';
import {Film} from "../../../models/dto/film-dto.model";

@Component({
  selector: 'app-attribute-list',
  templateUrl: './attribute-list.component.html',
  styleUrls: ['./attribute-list.component.scss']
})
export class AttributeListComponent implements OnInit {

  @Input() film: Film;

  constructor() {
  }

  ngOnInit(): void {
  }

}
