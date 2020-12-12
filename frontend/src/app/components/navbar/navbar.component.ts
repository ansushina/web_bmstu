import {Component, Input, OnInit} from '@angular/core';
import {User} from "../../models/dto/user-dto.model";

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  @Input() public user: User;
  constructor() { }

  ngOnInit(): void {
  }
}
