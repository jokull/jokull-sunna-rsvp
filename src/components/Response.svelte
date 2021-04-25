<script>
  export let guests;
  export let comment;
  export let email;
  export let deleted;
  export let toggleDeleted;
  $: visible = !deleted;
</script>

<div class="border-b pb-4 mb-4">
  <div class="flex">
    <div class={`flex-grow ${!visible && "opacity-20"}`}>
      <div class="mb-2">
        {#each guests as guest}
          <div class="flex items-center">
            <div
              class={`inline-flex items-center p-1 rounded-full text-xs font-medium ${
                guest.diet == "meat" && "bg-red-100 text-red-600"
              } ${guest.diet == "pescatarian" && "bg-blue-100 text-blue-600"} ${
                guest.diet == "vegan" && "bg-green-100 text-green-600"
              }`}
            >
              <svg class="h-2.5 w-2.5" fill="currentColor" viewBox="0 0 8 8">
                <circle cx="4" cy="4" r="3" />
              </svg>
            </div>
            <div class="font-semibold inline ml-1.5">{guest.name}</div>
          </div>
        {/each}
      </div>
      <div>
        <div class="flex items-center">
          <svg
            class="flex-shrink-0 mr-1.5 h-5 w-5 text-gray-400"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
          >
            <path
              d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"
            />
            <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
          </svg>
          <div class="text-sm text-gray-500">{email}</div>
        </div>
        {#if comment}
          <div
            class="text-sm my-2 px-2 py-1.5 rounded-lg rounded-bl-none inline-block bg-gray-100"
          >
            {comment}
          </div>
        {/if}
      </div>
    </div>
    <div>
      <button
        class="p-1 px-2.5 mr-2 rounded-full text-xs font-medium bg-gray-100 text-gray-600"
        on:click={() => {
          toggleDeleted(visible);
        }}>{visible ? "Fela" : "Sýna"}</button
      >
    </div>
  </div>
</div>
