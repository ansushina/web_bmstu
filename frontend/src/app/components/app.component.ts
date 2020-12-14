import {Component} from '@angular/core';
import {User} from '../models/dto/user-dto.model';
import {NavigationEnd, NavigationStart, Router} from '@angular/router';
import {UserService} from '../services/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  public user: User;
  title = 'frontend';

  constructor(private router: Router, private userService: UserService) {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationStart) {
        if (localStorage.getItem('username')) {
          this.userService.getUser(localStorage.getItem('username')).subscribe(
            user => this.user = user,
            error => {
              console.log(error);
              this.userService.logout();
            },
          );
        } else {
          this.user = null;
        }
      }
    });
  }

  onChange(): void {
    console.log('change');
  }

  ngOnInit(): void {
    console.log('app init');
    if (localStorage.getItem('username')) {
      this.userService.getUser(localStorage.getItem('username')).subscribe(
        user => this.user = user,
        error => {
          console.log(error);
          this.userService.logout();
        },
      );
    }
  }
}
