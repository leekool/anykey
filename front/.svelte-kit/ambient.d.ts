
// this file is generated — do not edit it


/// <reference types="@sveltejs/kit" />

/**
 * Environment variables [loaded by Vite](https://vitejs.dev/guide/env-and-mode.html#env-files) from `.env` files and `process.env`. Like [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), this module cannot be imported into client-side code. This module only includes variables that _do not_ begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env).
 * 
 * _Unlike_ [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), the values exported from this module are statically injected into your bundle at build time, enabling optimisations like dead code elimination.
 * 
 * ```ts
 * import { API_KEY } from '$env/static/private';
 * ```
 * 
 * Note that all environment variables referenced in your code should be declared (for example in an `.env` file), even if they don't have a value until the app is deployed:
 * 
 * ```
 * MY_FEATURE_FLAG=""
 * ```
 * 
 * You can override `.env` values from the command line like so:
 * 
 * ```bash
 * MY_FEATURE_FLAG="enabled" npm run dev
 * ```
 */
declare module '$env/static/private' {
	export const SHELL: string;
	export const npm_command: string;
	export const WINDOWID: string;
	export const npm_config_userconfig: string;
	export const COLORTERM: string;
	export const CSF_MDTVTexturesDirectory: string;
	export const npm_config_cache: string;
	export const CSF_DrawPluginDefaults: string;
	export const NODE: string;
	export const CSF_LANGUAGE: string;
	export const DOTNET_ROOT: string;
	export const SSH_AUTH_SOCK: string;
	export const CSF_MIGRATION_TYPES: string;
	export const GRADLE_HOME: string;
	export const INSIDE_EMACS: string;
	export const EMACS_VTERM_PATH: string;
	export const COLOR: string;
	export const npm_config_local_prefix: string;
	export const CSF_OCCTResourcePath: string;
	export const npm_config_globalconfig: string;
	export const CSF_STEPDefaults: string;
	export const EDITOR: string;
	export const GTK_MODULES: string;
	export const XDG_SEAT: string;
	export const PWD: string;
	export const LOGNAME: string;
	export const DRAWHOME: string;
	export const npm_config_init_module: string;
	export const SYSTEMD_EXEC_PID: string;
	export const CSF_StandardLiteDefaults: string;
	export const LIBGL_DRI3_DISABLE: string;
	export const MOTD_SHOWN: string;
	export const HOME: string;
	export const LANG: string;
	export const npm_package_version: string;
	export const STARSHIP_SHELL: string;
	export const INVOCATION_ID: string;
	export const MANAGERPID: string;
	export const INIT_CWD: string;
	export const CSF_ShadersDirectory: string;
	export const DOTNET_BUNDLE_EXTRACT_BASE_DIR: string;
	export const CSF_EXCEPTION_PROMPT: string;
	export const CSF_XmlOcafResource: string;
	export const STARSHIP_SESSION_KEY: string;
	export const ALACRITTY_SOCKET: string;
	export const npm_lifecycle_script: string;
	export const CSF_SHMessage: string;
	export const XDG_SESSION_CLASS: string;
	export const TERM: string;
	export const npm_package_name: string;
	export const npm_config_prefix: string;
	export const USER: string;
	export const CSF_StandardDefaults: string;
	export const CSF_IGESDefaults: string;
	export const DISPLAY: string;
	export const CSF_XCAFDefaults: string;
	export const npm_lifecycle_event: string;
	export const SHLVL: string;
	export const XDG_VTNR: string;
	export const CHROME_PATH: string;
	export const CSF_PluginDefaults: string;
	export const CSF_TObjMessage: string;
	export const XDG_SESSION_ID: string;
	export const npm_config_user_agent: string;
	export const CASROOT: string;
	export const npm_execpath: string;
	export const XDG_RUNTIME_DIR: string;
	export const DEBUGINFOD_URLS: string;
	export const npm_package_json: string;
	export const JOURNAL_STREAM: string;
	export const CSF_XSMessage: string;
	export const MMGT_CLEAR: string;
	export const npm_config_noproxy: string;
	export const BROWSER: string;
	export const PATH: string;
	export const npm_config_metrics_registry: string;
	export const CSF_TObjDefaults: string;
	export const npm_config_node_gyp: string;
	export const ALACRITTY_LOG: string;
	export const DBUS_SESSION_BUS_ADDRESS: string;
	export const npm_config_global_prefix: string;
	export const MAIL: string;
	export const ALACRITTY_WINDOW_ID: string;
	export const DRAWDEFAULT: string;
	export const npm_node_execpath: string;
	export const _: string;
	export const NODE_ENV: string;
}

/**
 * Similar to [`$env/static/private`](https://kit.svelte.dev/docs/modules#$env-static-private), except that it only includes environment variables that begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env) (which defaults to `PUBLIC_`), and can therefore safely be exposed to client-side code.
 * 
 * Values are replaced statically at build time.
 * 
 * ```ts
 * import { PUBLIC_BASE_URL } from '$env/static/public';
 * ```
 */
declare module '$env/static/public' {

}

/**
 * This module provides access to runtime environment variables, as defined by the platform you're running on. For example if you're using [`adapter-node`](https://github.com/sveltejs/kit/tree/master/packages/adapter-node) (or running [`vite preview`](https://kit.svelte.dev/docs/cli)), this is equivalent to `process.env`. This module only includes variables that _do not_ begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env).
 * 
 * This module cannot be imported into client-side code.
 * 
 * ```ts
 * import { env } from '$env/dynamic/private';
 * console.log(env.DEPLOYMENT_SPECIFIC_VARIABLE);
 * ```
 * 
 * > In `dev`, `$env/dynamic` always includes environment variables from `.env`. In `prod`, this behavior will depend on your adapter.
 */
declare module '$env/dynamic/private' {
	export const env: {
		SHELL: string;
		npm_command: string;
		WINDOWID: string;
		npm_config_userconfig: string;
		COLORTERM: string;
		CSF_MDTVTexturesDirectory: string;
		npm_config_cache: string;
		CSF_DrawPluginDefaults: string;
		NODE: string;
		CSF_LANGUAGE: string;
		DOTNET_ROOT: string;
		SSH_AUTH_SOCK: string;
		CSF_MIGRATION_TYPES: string;
		GRADLE_HOME: string;
		INSIDE_EMACS: string;
		EMACS_VTERM_PATH: string;
		COLOR: string;
		npm_config_local_prefix: string;
		CSF_OCCTResourcePath: string;
		npm_config_globalconfig: string;
		CSF_STEPDefaults: string;
		EDITOR: string;
		GTK_MODULES: string;
		XDG_SEAT: string;
		PWD: string;
		LOGNAME: string;
		DRAWHOME: string;
		npm_config_init_module: string;
		SYSTEMD_EXEC_PID: string;
		CSF_StandardLiteDefaults: string;
		LIBGL_DRI3_DISABLE: string;
		MOTD_SHOWN: string;
		HOME: string;
		LANG: string;
		npm_package_version: string;
		STARSHIP_SHELL: string;
		INVOCATION_ID: string;
		MANAGERPID: string;
		INIT_CWD: string;
		CSF_ShadersDirectory: string;
		DOTNET_BUNDLE_EXTRACT_BASE_DIR: string;
		CSF_EXCEPTION_PROMPT: string;
		CSF_XmlOcafResource: string;
		STARSHIP_SESSION_KEY: string;
		ALACRITTY_SOCKET: string;
		npm_lifecycle_script: string;
		CSF_SHMessage: string;
		XDG_SESSION_CLASS: string;
		TERM: string;
		npm_package_name: string;
		npm_config_prefix: string;
		USER: string;
		CSF_StandardDefaults: string;
		CSF_IGESDefaults: string;
		DISPLAY: string;
		CSF_XCAFDefaults: string;
		npm_lifecycle_event: string;
		SHLVL: string;
		XDG_VTNR: string;
		CHROME_PATH: string;
		CSF_PluginDefaults: string;
		CSF_TObjMessage: string;
		XDG_SESSION_ID: string;
		npm_config_user_agent: string;
		CASROOT: string;
		npm_execpath: string;
		XDG_RUNTIME_DIR: string;
		DEBUGINFOD_URLS: string;
		npm_package_json: string;
		JOURNAL_STREAM: string;
		CSF_XSMessage: string;
		MMGT_CLEAR: string;
		npm_config_noproxy: string;
		BROWSER: string;
		PATH: string;
		npm_config_metrics_registry: string;
		CSF_TObjDefaults: string;
		npm_config_node_gyp: string;
		ALACRITTY_LOG: string;
		DBUS_SESSION_BUS_ADDRESS: string;
		npm_config_global_prefix: string;
		MAIL: string;
		ALACRITTY_WINDOW_ID: string;
		DRAWDEFAULT: string;
		npm_node_execpath: string;
		_: string;
		NODE_ENV: string;
		[key: `PUBLIC_${string}`]: undefined;
		[key: string]: string | undefined;
	}
}

/**
 * Similar to [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), but only includes variables that begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env) (which defaults to `PUBLIC_`), and can therefore safely be exposed to client-side code.
 * 
 * Note that public dynamic environment variables must all be sent from the server to the client, causing larger network requests — when possible, use `$env/static/public` instead.
 * 
 * ```ts
 * import { env } from '$env/dynamic/public';
 * console.log(env.PUBLIC_DEPLOYMENT_SPECIFIC_VARIABLE);
 * ```
 */
declare module '$env/dynamic/public' {
	export const env: {
		[key: `PUBLIC_${string}`]: string | undefined;
	}
}
