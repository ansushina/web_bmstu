import {Component, Input, OnInit} from '@angular/core';
import {User} from "../../models/dto/user-dto.model";
import {ActivatedRoute, Router} from "@angular/router";
import {UserService} from "../../services/user.service";

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  @Input() public user: User;
  constructor(private route: ActivatedRoute, private router: Router, private userService: UserService) {
  }


  onExit(): void {
    this.userService.logout();
    this.router.navigate(['/home']);
  }

  ngOnInit(): void {
  }
}
