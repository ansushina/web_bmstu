import {Component, OnInit} from '@angular/core';
import {UserService} from '../../services/user.service';
import {ActivatedRoute, Router} from '@angular/router';
import {User} from '../../models/dto/user-dto.model';

@Component({
  selector: 'app-settings-page',
  templateUrl: './settings-page.component.html',
  styleUrls: ['./settings-page.component.scss']
})
export class SettingsPageComponent implements OnInit {

  public username: string;
  public email: string;
  public avatar: string;

  constructor(private route: ActivatedRoute, private router: Router, private userService: UserService) {
  }

  onChange(): void {
    const user = {
      email: this.email,
      avatar: this.avatar,
    };
    this.userService.updateUser(this.username, user).subscribe(
      newuser => {
        this.email = newuser.email;
        this.avatar = newuser.avatar;
      },
      error => console.log(error)
    );
  }

  ngOnInit(): void {
    if (localStorage.getItem('username')) {
      this.username = localStorage.getItem('username');
      this.userService.getUser(this.username).subscribe(
        user => {
          this.email = user.email;
          this.avatar = user.avatar
        },
        error => console.log(error),
      );
    } else {
      this.router.navigate(['/home']);
    }
  }

}
