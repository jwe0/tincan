<script>
    import { page } from '$app/stores';
</script>

<svelte:head>
    <title>Embed Generator</title>
    
    <!-- Open Graph -->
    <meta name="og:site_name" content={$page.url.searchParams.get("author")}>
    <meta name="og:type" content="object">
    <meta name="og:title" content={$page.url.searchParams.get("title")}>
    <meta property="og:image" content={$page.url.searchParams.get('thumbnail')}>
    <meta name="og:description" content={$page.url.searchParams.get("description")}>
    <meta name="og:url" content={$page.url.searchParams.get("url")}>
    <meta name="theme-color" content="#{$page.url.searchParams.get('colour')}">
</svelte:head>

