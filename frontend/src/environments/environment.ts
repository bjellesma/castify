// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  auth: {
    clientID: 'caolVXfgEL9z2t67IMOhcl10alFoRDQs',
    domain: 'dev-cpb64ukj.us.auth0.com',
    audience: 'https://127.0.0.1:5000',
    redirect: 'http://localhost:4200/callback',
    logout: 'http://localhost:4200',
    scope: 'openid profile email',
  },
  api_url: 'https://castifyio.herokuapp.com'
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
